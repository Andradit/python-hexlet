DROP TABLE IF EXISTS user_items;

CREATE TABLE user_items (
    id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username varchar(255) NOT NULL,
    item varchar(255) NOT NULL,
    received_at timestamp NOT NULL
);

INSERT INTO user_items (username, item, received_at) VALUES
('arya', 'Needle', NOW()),
('lord_mormont', 'Longclaw', NOW()),
('lord_mormont', 'The armor of the Nights Watch', NOW());
