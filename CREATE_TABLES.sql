CREATE TABLE aircrafts
(
    aircraft_code CHAR(3)     NOT NULL,
    model         VARCHAR(30) NOT NULL,
    `range`       INTEGER     NOT NULL,
    PRIMARY KEY (aircraft_code)
);

CREATE TABLE airports
(
    airport_code CHAR(3)     NOT NULL,
    airport_name VARCHAR(50) NOT NULL,
    city         VARCHAR(30) NOT NULL,
    coordinates  POINT       NOT NULL,
    timezone     TEXT        NOT NULL,
    PRIMARY KEY (airport_code)
);

CREATE TABLE boarding_passes
(
    ticket_no   CHAR(13)   NOT NULL,
    flight_id   INTEGER    NOT NULL,
    boarding_no INTEGER    NOT NULL,
    seat_no     VARCHAR(4) NOT NULL,
    PRIMARY KEY (ticket_no, flight_id),
    INDEX (flight_id, ticket_no)
);

CREATE TABLE bookings
(
    book_ref     CHAR(6)        NOT NULL,
    book_date    TIMESTAMP      NOT NULL,
    total_amount NUMERIC(10, 2) NOT NULL,
    PRIMARY KEY (book_ref)
);

CREATE TABLE flights
(
    flight_id           INTEGER     NOT NULL,
    flight_no           CHAR(6)     NOT NULL,
    scheduled_departure TIMESTAMP   NOT NULL,
    scheduled_arrival   TIMESTAMP   NOT NULL,
    departure_airport   CHAR(3)     NOT NULL,
    arrival_airport     CHAR(3)     NOT NULL,
    status              VARCHAR(20) NOT NULL,
    aircraft_code       CHAR(3)     NOT NULL,
    actual_departure    TIMESTAMP NULL,
    actual_arrival      TIMESTAMP NULL,
    PRIMARY KEY (flight_id),
    INDEX (departure_airport),
    INDEX (arrival_airport),
    INDEX (aircraft_code)
);

CREATE TABLE seats
(
    aircraft_code   CHAR(3)     NOT NULL,
    seat_no         VARCHAR(4)  NOT NULL,
    fare_conditions VARCHAR(10) NOT NULL,
    PRIMARY KEY (aircraft_code, seat_no),
    INDEX (aircraft_code)
);

CREATE TABLE ticket_flights
(
    ticket_no       CHAR(13)       NOT NULL,
    flight_id       INTEGER        NOT NULL,
    fare_conditions VARCHAR(10)    NOT NULL,
    amount          NUMERIC(10, 2) NOT NULL,
    PRIMARY KEY (ticket_no, flight_id),
    INDEX (flight_id),
    INDEX (ticket_no)
);

CREATE TABLE tickets
(
    ticket_no      CHAR(13)    NOT NULL,
    book_ref       CHAR(6)     NOT NULL,
    passenger_id   VARCHAR(20) NOT NULL,
    passenger_name TEXT        NOT NULL,
    phone          VARCHAR(20) NULL,
    PRIMARY KEY (ticket_no),
    INDEX (book_ref)
);


ALTER TABLE tickets
    ADD FOREIGN KEY (book_ref) REFERENCES bookings (book_ref) ON DELETE CASCADE;

ALTER TABLE boarding_passes
    ADD FOREIGN KEY (flight_id, ticket_no) REFERENCES ticket_flights (flight_id, ticket_no) ON DELETE CASCADE;

ALTER TABLE seats
    ADD FOREIGN KEY (aircraft_code) REFERENCES aircrafts (aircraft_code) ON DELETE CASCADE;

ALTER TABLE flights
    ADD FOREIGN KEY (departure_airport) REFERENCES airports (airport_code) ON DELETE CASCADE;

ALTER TABLE flights
    ADD FOREIGN KEY (arrival_airport) REFERENCES airports (airport_code) ON DELETE CASCADE;

ALTER TABLE flights
    ADD FOREIGN KEY (aircraft_code) REFERENCES aircrafts (aircraft_code) ON DELETE CASCADE;

ALTER TABLE ticket_flights
    ADD FOREIGN KEY (flight_id) REFERENCES flights (flight_id) ON DELETE CASCADE;

ALTER TABLE ticket_flights
    ADD FOREIGN KEY (ticket_no) REFERENCES tickets (ticket_no) ON DELETE CASCADE;