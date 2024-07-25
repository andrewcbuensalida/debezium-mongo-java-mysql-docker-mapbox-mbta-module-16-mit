CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id varchar(255),
    latitude decimal(11,8),
    longitude decimal(11,8),
    occupancy_status varchar(255),
    current_status varchar(255),
    bikes_allowed INT, -- 0, 1, 2
    headsign varchar(255),
    bearing decimal(11,8), -- 0 is North and 90 is East.
    current_stop_sequence INT,
    updated_at TIMESTAMP -- mbta api has a timezone of -04:00 so have to set the timezone in the mysql container. Then when using pandas pd.read_sql_query, manually set the update_at column with df['updated_at'].dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
);

