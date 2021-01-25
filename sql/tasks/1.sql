SELECT airports.city as city, SUM(cancelled.cancelled_flights) as cancelled_flights_num
FROM airports
         INNER JOIN
     (SELECT departure_airport, COUNT(*) as cancelled_flights
      FROM flights
      WHERE status = 'Cancelled'
      GROUP BY departure_airport)
         as cancelled
     ON airports.airport_code = cancelled.departure_airport
GROUP BY city
ORDER BY cancelled_flights_num DESC
LIMIT 5;