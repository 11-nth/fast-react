-- Creating the users table
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL
);

-- Creating the accounts table
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    account_name VARCHAR(255) NOT NULL
);

-- Creating the account_user_mapping table
CREATE TABLE account_user_mapping (
    mapping_id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users (user_id) ON DELETE CASCADE,
    account_id INTEGER REFERENCES accounts (account_id) ON DELETE CASCADE
);

-- Creating the account_partition table
CREATE TABLE account_partition (
    partition_id INTEGER PRIMARY KEY,
    account_id INTEGER REFERENCES accounts (account_id) ON DELETE CASCADE,
    partition_name VARCHAR(255) NOT NULL
);

-- Creating the transaction_table
CREATE TABLE transaction_table (
    txn_id INTEGER PRIMARY KEY,
    txn_name VARCHAR(255) NOT NULL,
    paid_by_account_id INTEGER REFERENCES accounts (account_id) ON DELETE CASCADE,
    paid_for_account_id INTEGER REFERENCES accounts (account_id) ON DELETE CASCADE,
    amount INTEGER NOT NULL
);