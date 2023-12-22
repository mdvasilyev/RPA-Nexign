create table robot (
    robot_id serial primary key,
    name varchar(255),
    description text
);

create table worker (
    worker_id serial primary key,
    name varchar(255),
    path varchar(255),
    description text
);

create table location (
    location_id serial primary key,
    robot_id int references robot(robot_id),
    worker_id int references worker(worker_id)
);

create table components (
    components_id serial primary key,
    robot_id int references robot(robot_id),
    robot_conf_name varchar(255),
    robot_conf bytea,
    env_conf_name varchar(255),
    env_conf bytea,
    main_name varchar(255),
    main bytea,
    locators_name varchar(255),
    locators bytea
);

create table images (
    images_id serial primary key,
    components_id int references components(components_id),
    name varchar(255),
    contents bytea
);