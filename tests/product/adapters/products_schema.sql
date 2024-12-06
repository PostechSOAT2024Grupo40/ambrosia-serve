CREATE TABLE products
(
  id          SERIAL PRIMARY KEY,
  sku         TEXT      NOT NULL UNIQUE,
  description TEXT      NOT NULL,
  category    TEXT      NOT NULL,
  price       NUMERIC   NOT NULL,
  stock       INTEGER   NOT NULL,
  created_at  TIMESTAMP NOT NULL DEFAULT now(),
  updated_at  TIMESTAMP NOT NULL DEFAULT now()
);

