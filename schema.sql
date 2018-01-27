-- This file contains the definitions of the tables used in the application
--

    create table user_table(                    -- user of system (inherit administrator, supplier and client)
    u_id serial primary key,         -- user id
    u_email varchar(50),             -- user email
    u_password varchar(20),         -- user password
    u_name varchar(20),          -- user name
    u_lastname varchar(20),          -- user last name
    u_region varchar(20),          -- user location
    u_age int                 -- user age to see if user is older than 18 years old
    );

    create table administrator(                -- administers the system (inherited from users)
    ad_id serial primary key         -- administrator id
    ) INHERITS (user_table);

    create table supplier(                -- supplies by announcements (inherited from users)
    s_id serial primary key,         -- supplier id
    s_bank_account integer            -- supplier bank account
    ) INHERITS (user_table);

    create table client(                    -- client get donations or purchases (inherited from users)
    c_id serial primary key         -- client id
    ) INHERITS (user_table);

    create table address(                --address of user
    add_id serial primary key,         --address id
    c_id integer references client(c_id),    --user id
    add_line1 varchar(25),        --address line 1
    add_line2 varchar(25),        --address line 2
    add_city varchar(20),        --address town
    add_country varchar(20),         --address country
    add_zip_code char(5)            --address zip code
    );

    create table credit_card(                -- credit card registered by a supplier (can own more)
    cc_id serial primary key,         -- credit card id
    c_id integer references client(c_id),    --client id
    cc_name varchar(20),         -- credit card name
    cc_lastname varchar(20),        -- credit card last name
    cc_number integer,             -- credit card number
    cc_exp_date Date            -- credit card expiration date
    );

    create table resource(                -- resource of system
    r_id serial primary key,         -- resource id
    r_category varchar(20),         -- resource category
    r_name varchar(20),             -- resource name
    r_description varchar(50)        -- resource description
    );

    create table transaction(                -- transaction made between supplier and client
    t_id serial primary key,         -- transaction id
    s_id integer references supplier(s_id),     -- supplier id
    c_id integer references client(c_id),         -- client id
    r_id integer references resource(r_id),    --resource id
    t_price float,                 -- transaction price
    t_date Date,                 -- transaction date
    t_qty int                -- transaction quantity (of resources)
    );

    create table announcement(            -- announcement made by a supplier
    a_id serial primary key,         -- announcement id
    s_id integer references supplier(s_id),    -- supplier id
    r_id integer references resource(r_id),    --resource id
    a_price float,                 -- announcement price per unit
    a_date Date,                 -- announcement date
    a_sold_out boolean,             -- announcement status (if sold out or not)
    a_initial_qty int,             -- announcement initial quantity
    a_curr_qty int                -- announcement current quantity
    );

    create table request(                -- request made by a supplier
    req_id serial primary key,         -- request id
    c_id integer references client(c_id),         -- client id
    r_id integer references resource(r_id),        --resource id
    req_qty int,                 -- request quantity
    req_date Date                -- request date
    );