abi = [
    {
      "inputs": [
        {
          "internalType": "contract IERC20",
          "name": "settlementTokenInStableCoin",
          "type": "address"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "userAddress",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "contactAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "email",
          "type": "string"
        }
      ],
      "name": "ContactAdded",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "expenseId",
          "type": "bytes32"
        },
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "groupId",
          "type": "bytes32"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "paidByUserAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "description",
          "type": "string"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "createdAtTimestamp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address[]",
          "name": "memberAddresses",
          "type": "address[]"
        }
      ],
      "name": "ExpenseCreated",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "groupId",
          "type": "bytes32"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "ownerAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "description",
          "type": "string"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "createdAtTimestamp",
          "type": "uint256"
        }
      ],
      "name": "GroupCreated",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "settlementId",
          "type": "bytes32"
        },
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "groupId",
          "type": "bytes32"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "settledByUserAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "createdAtTimestamp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address[]",
          "name": "memberAddresses",
          "type": "address[]"
        }
      ],
      "name": "SettlementCreated",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "userAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "email",
          "type": "string"
        }
      ],
      "name": "UserProfileUpdated",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "contactAddress",
          "type": "address"
        },
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "email",
          "type": "string"
        }
      ],
      "name": "addContact",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "groupId",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "memberAddress",
          "type": "address"
        }
      ],
      "name": "addGroupMembership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "groupId",
          "type": "bytes32"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "description",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "createdAtTimestamp",
          "type": "uint256"
        },
        {
          "internalType": "address[]",
          "name": "memberAddresses",
          "type": "address[]"
        }
      ],
      "name": "createExpense",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "description",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "createdAtTimestamp",
          "type": "uint256"
        },
        {
          "internalType": "address[]",
          "name": "memberAddresses",
          "type": "address[]"
        }
      ],
      "name": "createGroup",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "expenseId",
          "type": "bytes32"
        }
      ],
      "name": "getExpense",
      "outputs": [
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "expenseId",
              "type": "bytes32"
            },
            {
              "internalType": "bytes32",
              "name": "groupId",
              "type": "bytes32"
            },
            {
              "internalType": "address",
              "name": "paidByUserAddress",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "amount",
              "type": "uint256"
            },
            {
              "internalType": "string",
              "name": "description",
              "type": "string"
            },
            {
              "internalType": "uint256",
              "name": "createdAtTimestamp",
              "type": "uint256"
            },
            {
              "internalType": "address[]",
              "name": "memberAddresses",
              "type": "address[]"
            }
          ],
          "internalType": "struct SplitSum.Expense",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "groupId",
          "type": "bytes32"
        }
      ],
      "name": "getGroup",
      "outputs": [
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "groupId",
              "type": "bytes32"
            },
            {
              "internalType": "address",
              "name": "ownerAddress",
              "type": "address"
            },
            {
              "internalType": "string",
              "name": "name",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "description",
              "type": "string"
            },
            {
              "internalType": "uint256",
              "name": "createdAtTimestamp",
              "type": "uint256"
            },
            {
              "internalType": "address[]",
              "name": "memberAddresses",
              "type": "address[]"
            }
          ],
          "internalType": "struct SplitSum.Group",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "settlementId",
          "type": "bytes32"
        }
      ],
      "name": "getSettlement",
      "outputs": [
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "settlementId",
              "type": "bytes32"
            },
            {
              "internalType": "bytes32",
              "name": "groupId",
              "type": "bytes32"
            },
            {
              "internalType": "address",
              "name": "settledByUserAddress",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "amount",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "createdAtTimestamp",
              "type": "uint256"
            },
            {
              "internalType": "address[]",
              "name": "memberAddresses",
              "type": "address[]"
            }
          ],
          "internalType": "struct SplitSum.Settlement",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getUserProfile",
      "outputs": [
        {
          "components": [
            {
              "internalType": "address",
              "name": "userAddress",
              "type": "address"
            },
            {
              "internalType": "string",
              "name": "name",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "email",
              "type": "string"
            }
          ],
          "internalType": "struct SplitSum.User",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "listContacts",
      "outputs": [
        {
          "components": [
            {
              "internalType": "address",
              "name": "userAddress",
              "type": "address"
            },
            {
              "internalType": "string",
              "name": "name",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "email",
              "type": "string"
            }
          ],
          "internalType": "struct SplitSum.User[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "expenseId",
          "type": "bytes32"
        }
      ],
      "name": "listExpenseMembers",
      "outputs": [
        {
          "components": [
            {
              "internalType": "address",
              "name": "memberAddress",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "amount",
              "type": "uint256"
            }
          ],
          "internalType": "struct SplitSum.ExpenseMember[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "groupId",
          "type": "bytes32"
        }
      ],
      "name": "listGroupMemberships",
      "outputs": [
        {
          "components": [
            {
              "internalType": "address",
              "name": "memberAddress",
              "type": "address"
            },
            {
              "internalType": "int256",
              "name": "balance",
              "type": "int256"
            }
          ],
          "internalType": "struct SplitSum.Membership[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "listMembershipGroups",
      "outputs": [
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "groupId",
              "type": "bytes32"
            },
            {
              "internalType": "address",
              "name": "ownerAddress",
              "type": "address"
            },
            {
              "internalType": "string",
              "name": "name",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "description",
              "type": "string"
            },
            {
              "internalType": "uint256",
              "name": "createdAtTimestamp",
              "type": "uint256"
            },
            {
              "internalType": "address[]",
              "name": "memberAddresses",
              "type": "address[]"
            }
          ],
          "internalType": "struct SplitSum.Group[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "settlementId",
          "type": "bytes32"
        }
      ],
      "name": "listSettlementMembers",
      "outputs": [
        {
          "components": [
            {
              "internalType": "address",
              "name": "memberAddress",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "amount",
              "type": "uint256"
            }
          ],
          "internalType": "struct SplitSum.SettlementMember[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "groupId",
          "type": "bytes32"
        },
        {
          "internalType": "address",
          "name": "memberAddress",
          "type": "address"
        }
      ],
      "name": "removeGroupMembership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "groupId",
          "type": "bytes32"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "createdAtTimestamp",
          "type": "uint256"
        }
      ],
      "name": "settleUp",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "email",
          "type": "string"
        }
      ],
      "name": "updateUserProfile",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]