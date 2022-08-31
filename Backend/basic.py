from email.policy import default
from venv import create
from flask import Flask, request, render_template, json
from flask_restx import Api, Resource, reqparse
from sc import *


app = Flask(__name__)
api = Api(app, title='SplitSum')

splitsum = api.namespace('', description='List of SplitSum methods')

db_contacts = 'db_contacts.json'
db_transactions = 'db_transactions.json'
db_groups = 'db_groups.json'

parser_contacts = reqparse.RequestParser()
parser_contacts.add_argument('name', type=str, help='Name of user', required=True)
parser_contacts.add_argument('email', type=str, help='Email address', default="None")
parser_contacts.add_argument('wallet_address', type=str, help='Wallet address', required=True)
@splitsum.route('/contacts')
class Contacts(Resource):
    @splitsum.doc(description="Get all contacts")
    def get(self):
        with open(db_contacts) as db:
            contacts = json.load(db)
        return {"contacts":list(contacts.values())}
    @splitsum.doc(parser=parser_contacts, description="Create new contact")
    def post(self):
        args = parser_contacts.parse_args()
        name = args['name']
        email = args['email']
        wallet_address = args['wallet_address']
        tx_success = add_contact(name, email, wallet_address)
        if tx_success == 0:
            return {"message": "transaction failed"}
        else :
            with open(db_contacts) as db:
                contacts = json.load(db)
            keys = []
            for key, value in contacts.items():
                keys.append(int(key))
            item_id = str(max(keys) + 1) or 1
            new_contact_info = {"user_id":int(item_id), "name": name, "email":email, 
                            "wallet_address": wallet_address}
            contacts[item_id] = new_contact_info      
            with open(db_contacts, 'w') as db_w:
                json.dump(contacts, db_w)
            return new_contact_info


parser_transactions = reqparse.RequestParser()
parser_transactions.add_argument('group_id', type=str, help='Group that user belongs to', required=True)

@splitsum.route('/transactions')
class Transactions(Resource):
    @splitsum.doc(parser=parser_transactions, description="Get all transactions for group of user")
    def get(self):
        args = parser_transactions.parse_args()
        group_id = args['group_id']
        with open(db_transactions) as db:
            transactions = json.load(db)
        group_tx = {}
        for key, value in transactions.items():
            for key1, value1 in value.items():
                if (key1 == 'group_id' and value1 == group_id):
                    group_tx[key] = value
        return {"transactions":list(group_tx.values())}

parser_expense = reqparse.RequestParser()
parser_expense.add_argument('group_id', type=str, help='Group that user belongs to', required=True)
parser_expense.add_argument('amount', type=int, help='Amount of expense', required=True)
parser_expense.add_argument('share_members', type=str, help='List of users to split with', required=True, action="append")
parser_expense.add_argument('description', type=str, help='Group description')
@splitsum.route('/transactions/expense')
class TransactionsExpense(Resource):
    @splitsum.doc(parser=parser_expense, description="Create an expense transaction")
    def post(self):
        args = parser_expense.parse_args()
        group_id = args['group_id']
        amount = args['amount']
        share_members = args['share_members']
        description = args['description']
        created_at, tx_success = create_expense(group_id, amount, description, share_members)

        if tx_success == 0:
            return {"message": "transaction failed"}
        else:
            new_expense = {"group_id": group_id, "amount":amount, 
                            "share_members":share_members, "created_at": created_at,
                            "description":description, "type":"expense"
                        }

            with open(db_transactions) as db:
                transactions = json.load(db)
            keys = []
            for key, value in transactions.items():
                keys.append(int(key))
            item_id = str(max(keys) + 1) or 1
            transactions[item_id] = new_expense      
            with open(db_transactions, 'w') as db_w:
                json.dump(transactions, db_w)
            return new_expense


parser_settlement = reqparse.RequestParser()
parser_settlement.add_argument('group_id', type=str, help='Group that user belongs to', required=True)
parser_settlement.add_argument('amount', type=int, help='Amount of expense', required=True)
@splitsum.route('/transactions/settlement')
class TransactionsSettlement(Resource):
    @splitsum.doc(parser=parser_settlement, description="Create a settlement transaction")
    def post(self):
        args = parser_settlement.parse_args()
        group_id = args['group_id']
        amount = args['amount']

        created_at, tx_success, payer = settle_expense(group_id, amount)
        if tx_success == 0:
            return {"message": "transaction failed"}
        else:
            new_settlement = {"group_id": group_id, "amount":amount, 
                            "created_at":created_at, "paid_by":payer, "type":"settlement"
                        }

            with open(db_transactions) as db:
                transactions = json.load(db)
            keys = []
            for key, value in transactions.items():
                keys.append(int(key))
            item_id = str(max(keys) + 1) or 1
            transactions[item_id] = new_settlement  
            for key, value in transactions.items():
                for key1, value1 in value1.items():
                    if key1 == 'group_id':
                        if value1 == group_id:
                            member_index = transactions[key][key1].index(payer)
                            transactions[key][key1].pop(member_index)
                    if key1 == 'amount':
                        transactions[key][key1] = transactions[key][key1] - amount
                    
            with open(db_transactions, 'w') as db_w:
                json.dump(transactions, db_w)
            return new_settlement

parser_group = reqparse.RequestParser()
parser_group.add_argument('name', type=str, help='Name of group', required=True)
parser_group.add_argument('members', type=str, help='List of users in group - Input wallet address', action="append")
parser_group.add_argument('description', type=str, help='Group description')
# Add owner to group
@splitsum.route('/groups')
class Groups(Resource):
    @splitsum.doc(description="Get all Groups")
    def get(self):
        with open(db_groups) as db:
            groups = json.load(db)
        return {"groups":list(groups.values())}
    @splitsum.doc(parser=parser_group, description="Create a group")
    def post(self):
        args = parser_group.parse_args()
        name = args['name']
        members = args['members']
        description = args['description']
        print(name)
        print(members)
        print(description)
        group_id_hash, created_at, tx_success, owner = create_group(name=name, description=description, member_addresses=members)

        members.append(owner)
        if tx_success == 0:
            return {"message": "transaction failed"}
        else:
            with open(db_groups) as db:
                groups = json.load(db)
            keys = []
            for key, value in groups.items():
                keys.append(int(key))
            group_id = str(max(keys) + 1) or 1
            

            new_group = {"group_id": group_id_hash, "name":name, 
                            "created_at": created_at, "members":members,
                            "description":description
                        }
            groups[group_id] = new_group
            with open(db_groups, 'w') as db_w:
                json.dump(groups, db_w)
            return new_group


parser_group_membership = reqparse.RequestParser()
parser_group_membership.add_argument('group_id', type=str, help='hash of group', required=True)
parser_group_membership.add_argument('member', type=str, help='User to add to group - Input wallet address')

@splitsum.route('/groups/membership/add')
class GroupsMembershipAdd(Resource):
    @splitsum.doc(parser=parser_group_membership, description="Add member to group")
    def post(self):
        args = parser_group_membership.parse_args()
        group_id = args['group_id']
        member = args['member']

        tx_success = add_group_membership(group_id, member)

        if tx_success == 0:
            return {"message": "transaction failed"}
        else:
            id = None
            with open(db_groups) as db:
                groups = json.load(db)
            for key, value in groups.items():
                # print(key, value)
                for key1, value1 in value.items():
                    # print(key1, value1)
                    if key1 == 'group_id':
                        if value1 == group_id:
                            id = key
            if id != None:
                groups[id]['members'].append(member)
            with open(db_groups, 'w') as db_w:
                    json.dump(groups, db_w)
            return {"groups":list(groups[id].values())}


parser_group_membership_remove = reqparse.RequestParser()
parser_group_membership_remove.add_argument('group_id', type=str, help='hash of group', required=True)
parser_group_membership_remove.add_argument('member', type=str, help='User to remove from group - Input wallet address')
@splitsum.route('/groups/membership/remove')
class GroupsMembershipRemove(Resource):
    @splitsum.doc(parser=parser_group_membership_remove, description="Add member to group")
    def post(self):
        args = parser_group_membership_remove.parse_args()
        group_id = args['group_id']
        member = args['member']

        tx_success = remove_group_membership(group_id, member)

        if tx_success == 0:
            return {"message": "transaction failed"}
        else:
            id = None
            with open(db_groups) as db:
                groups = json.load(db)
            for key, value in groups.items():
                # print(key, value)
                for key1, value1 in value.items():
                    # print(key1, value1)
                    if key1 == 'group_id':
                        if value1 == group_id:
                            id = key
            if id != None:
                if member in groups[id]['members']:
                    member_index = groups[id]['members'].index(member)
                    groups[id]['members'].pop(member_index)
                # groups[id]['members'].append(member)
            with open(db_groups, 'w') as db_w:
                    json.dump(groups, db_w)
            return {"groups":list(groups[id].values())}
 
if __name__ == '__main__':
    app.run()





# @app.route('/contacts', methods=['GET', 'POST'])
# def list_contacts():
#     if request.method == 'GET':
#         return {"contacts":list(contacts_example.values())}
#     elif request.method == 'POST':
#         return create_contact(request.get_json(force=True))

# def create_contact(new_contact):
#    contact_name = new_contact['name']
#    contacts_example[contact_name] = new_contact
#    return new_contact


# # Sample payload:
# # curl -X POST http://127.0.0.1:5000/contacts -H 'Content-Type: application/json' -d '{"name": "Ron", "email": "", "wallet_address": "0x42a4C12C3Bc6e70d6a58f159B69c175f13608379"}'


# @api.route('/groups/<int:group_id>/transactions', methods=['GET'])
# def list_transactions(group_id):
#     if request.method == 'GET':
#         group_tx = {}
#         for key, value in transactions_example.items():
#             for key1, value1 in value.items():
#                 if (key1 == 'group_id' and value1 == group_id):
#                     group_tx[key] = value
#         return {"transactions":list(group_tx.values())}


# @api.route('/groups/<int:group_id>/expenses', methods=['POST'])
# def post_expense(group_id):
#     if request.method == 'POST':
#         return create_expense(request.get_json(force=True))

