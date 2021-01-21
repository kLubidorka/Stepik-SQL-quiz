CREATE TABLE aircrafts
(
    aircraft_code CHAR(3) PRIMARY KEY NOT NULL,
    model         VARCHAR(30)         NOT NULL,
    range         INTEGER             NOT NULL
);

CREATE TABLE airports
(
    airport_code CHAR(3) PRIMARY KEY NOT NULL,
    airport_name VARCHAR(30)         NOT NULL,
    city         VARCHAR(30)         NOT NULL,
    coordinates  POINT               NOT NULL,
    timezone     TEXT                NOT NULL
);

CREATE TABLE boarding_passes
(
    ticket_no   CHAR(13)   NOT NULL,
    flight_id   INTEGER    NOT NULL,
    boarding_no INTEGER    NOT NULL,
    seat_no     VARCHAR(4) NOT NULL,
    PRIMARY KEY (ticket_no, flight_id)
);

CREATE TABLE bookings
(
    book_ref     CHAR(6) PRIMARY KEY NOT NULL,
    book_date    TIMESTAMP           NOT NULL,
    total_amount NUMERIC(10, 2)      NOT NULL
);

CREATE TABLE flights
(
    flight_id           VARCHAR(10) PRIMARY KEY NOT NULL,
    flight_no           CHAR(6)                 NOT NULL,
    scheduled_departure TIMESTAMP               NOT NULL,
    scheduled_arrival   TIMESTAMP               NOT NULL,
    departure_airport   CHAR(3)                 NOT NULL,
    arrival_airport     CHAR(3)                 NOT NULL,
    status              VARCHAR(20)             NOT NULL,
    aircraft_code       CHAR(3)                 NOT NULL,
    actual_departure    TIMESTAMP NULL,
    actual_arrival      TIMESTAMP NULL
);

CREATE TABLE seats
(
    aircraft_code   CHAR(3)     NOT NULL,
    seat_no         VARCHAR(4)  NOT NULL,
    fare_conditions VARCHAR(10) NOT NULL,
    PRIMARY KEY (aircraft_code, seat_no)
);

CREATE TABLE ticket_flights
(
    ticket_no       CHAR(13)       NOT NULL,
    flight_id       INTEGER        NOT NULL,
    fare_conditions VARCHAR(10)    NOT NULL,
    amount          NUMERIC(10, 2) NOT NULL,
    PRIMARY KEY (ticket_no, flight_id)
);

CREATE TABLE tickets
(
    ticket_no      CHAR(13) PRIMARY KEY NOT NULL,
    book_ref       CHAR(6)              NOT NULL,
    passenger_id   VARCHAR(20)          NOT NULL,
    passenger_name TEXT                 NOT NULL,
    contact_data   JSON NULL
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

ALTER TABLE ticket_flights
    ADD FOREIGN KEY (flight_id) REFERENCES flights (flight_id) ON DELETE CASCADE;

ALTER TABLE ticket_flights
    ADD FOREIGN KEY (ticket_no) REFERENCES tickets (ticket_no) ON DELETE CASCADE;