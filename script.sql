create table admins
(
    id         int auto_increment
        primary key,
    username   varchar(50)                         not null,
    password   varchar(255)                        not null,
    email      varchar(100)                        not null,
    created_at timestamp default CURRENT_TIMESTAMP null,
    constraint email
        unique (email),
    constraint username
        unique (username)
);

create table menu
(
    id            int auto_increment
        primary key,
    dish_name     varchar(255)                       not null,
    cuisine_type  varchar(100)                       null,
    creation_time datetime default CURRENT_TIMESTAMP null,
    recipe_text   text                               null,
    recipe_image  longblob                           null
);

create table users
(
    id            int auto_increment
        primary key,
    username      varchar(200)                        not null,
    password      varchar(255)                        not null,
    email         varchar(100)                        not null,
    phone         varchar(20)                         null,
    registered_at timestamp default CURRENT_TIMESTAMP null,
    constraint email
        unique (email),
    constraint username
        unique (username)
);


