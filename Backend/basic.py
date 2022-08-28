from flask import Flask, request, render_template, json
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app, title='SplitSum')

splitsum = api.namespace('SplitSum', description='SplitSum methods')

db_contacts = 'db_contacts.json'
db_transactions = 'db_transactions.json'
db_groups = 'db_groups.json'

parser_contacts = reqparse.RequestParser()
parser_contacts.add_argument('name', type=str, help='Name of user', required=True)
parser_contacts.add_argument('email', type=str, help='Email address')
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
        new_contact_info = {"name": name, "email":email, 
                        "wallet_address": wallet_address}

        with open(db_contacts) as db:
            contacts = json.load(db)
        keys = []
        for key, value in contacts.items():
            keys.append(int(key))
        item_id = str(max(keys) + 1)
        contacts[item_id] = new_contact_info      
        with open(db_contacts, 'w') as db_w:
            json.dump(contacts, db_w)
        return new_contact_info


parser_transactions = reqparse.RequestParser()
parser_transactions.add_argument('group_id', type=int, help='Group that user belongs to', required=True)

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
parser_expense.add_argument('group_id', type=int, help='Group that user belongs to', required=True)
parser_expense.add_argument('amount', type=int, help='Amount of expense', required=True)
parser_expense.add_argument('currency', type=str, help='Currency being used', required=True)
parser_expense.add_argument('share_members', type=str, help='List of users to split with', required=True, action="append")
parser_expense.add_argument('description', type=str, help='Group description')
parser_expense.add_argument('paid_by', type=str, help='User that paid', required=True)
@splitsum.route('/transactions/expense')
class TransactionsExpense(Resource):
    @splitsum.doc(parser=parser_expense, description="Create an expense transaction")
    def post(self):
        args = parser_expense.parse_args()
        group_id = args['group_id']
        amount = args['amount']
        currency = args['currency']
        share_members = args['share_members']
        description = args['description']
        paid_by = args['paid_by']

        new_expense = {"group_id": group_id, "amount":amount, 
                        "currency": currency, "share_members":share_members,
                        "description":description, "paid_by":paid_by, "type":"expense"
                    }

        with open(db_transactions) as db:
            transactions = json.load(db)
        keys = []
        for key, value in transactions.items():
            keys.append(int(key))
        item_id = str(max(keys) + 1)
        transactions[item_id] = new_expense      
        with open(db_transactions, 'w') as db_w:
            json.dump(transactions, db_w)
        return new_expense


parser_settlement = reqparse.RequestParser()
parser_settlement.add_argument('group_id', type=int, help='Group that user belongs to', required=True)
parser_settlement.add_argument('amount', type=int, help='Amount of expense', required=True)
parser_settlement.add_argument('currency', type=str, help='Currency being used', required=True)
parser_settlement.add_argument('signature', type=str, help='Signature', required=True)
parser_settlement.add_argument('token_address', type=str, help='Group description')
parser_settlement.add_argument('paid_by', type=str, help='User that paid', required=True)
@splitsum.route('/transactions/settlement')
class TransactionsSettlement(Resource):
    @splitsum.doc(parser=parser_settlement, description="Create a settlement transaction")
    def post(self):
        args = parser_settlement.parse_args()
        group_id = args['group_id']
        amount = args['amount']
        currency = args['currency']
        signature = args['signature']
        token_address = args['token_address']
        paid_by = args['paid_by']

        new_settlement = {"group_id": group_id, "amount":amount, 
                        "currency": currency, "signature":signature,
                        "token_address":token_address, "paid_by":paid_by, "type":"settlement"
                    }

        with open(db_transactions) as db:
            transactions = json.load(db)
        keys = []
        for key, value in transactions.items():
            keys.append(int(key))
        item_id = str(max(keys) + 1)
        transactions[item_id] = new_settlement      
        with open(db_transactions, 'w') as db_w:
            json.dump(transactions, db_w)
        return new_settlement

parser_group = reqparse.RequestParser()
parser_group.add_argument('name', type=str, help='Name of group', required=True)
parser_group.add_argument('currency', type=str, help='Currency being used', required=True)
parser_group.add_argument('members', type=str, help='List of users in group', required=True, action="append")
parser_group.add_argument('description', type=str, help='Group description')
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
        currency = args['currency']
        description = args['description']

        with open(db_groups) as db:
            groups = json.load(db)
        keys = []
        for key, value in groups.items():
            keys.append(int(key))
        group_id = str(max(keys) + 1)
        

        new_group = {"group_id": group_id, "name":name, 
                        "currency": currency, "members":members,
                        "description":description
                    }
        groups[group_id] = new_group
        with open(db_groups, 'w') as db_w:
            json.dump(groups, db_w)
        return new_group


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

