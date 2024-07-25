CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id varchar(255) not null,
    latitude decimal(11,8) not null,
    longitude decimal(11,8) not null,
    occupancy_status varchar(255) not null,
    current_status varchar(255) not null,
    bikes_allowed INT, -- 0, 1, 2
    headsign varchar(255) not null,
    bearing decimal(11,8) not null, -- 0 is North and 90 is East.
    current_stop_sequence INT not null,
    updated_at TIMESTAMP not null
);

