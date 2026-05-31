{% set film_title = 'Inception' %}

WITH selected_film AS (
    SELECT *
    FROM {{ ref('films') }}
    WHERE title = '{{ film_title }}'
)

SELECT
    f.*,
    a.actor_name
FROM selected_film f
LEFT JOIN {{ ref('film_actors') }} fa
    ON f.film_id = fa.film_id
LEFT JOIN {{ ref('actors') }} a
    ON fa.actor_id = a.actor_id