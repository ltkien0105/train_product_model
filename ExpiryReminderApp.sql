CREATE TABLE "users" (
  "id" SERIAL PRIMARY KEY,
  "fullname" VARCHAR NOT NULL,
  "email" VARCHAR UNIQUE NOT NULL,
  "password_hash" VARCHAR NOT NULL,
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE "categories" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR UNIQUE NOT NULL,
	"parent" INT NOT NULL DEFAULT -1
);
INSERT INTO "categories" VALUES (1, 'Beverages', -1);
INSERT INTO "categories" VALUES (2, 'Condiments & Sauces', -1);
INSERT INTO "categories" VALUES (3, 'Dairy & Alternatives', -1);
INSERT INTO "categories" VALUES (4, 'Fruits', -1);
INSERT INTO "categories" VALUES (5, 'Proteins', -1);
INSERT INTO "categories" VALUES (6, 'Snacks & Sweets', -1);
INSERT INTO "categories" VALUES (7, 'Staples & Grains', -1);
INSERT INTO "categories" VALUES (8, 'Vegetables', -1);

INSERT INTO "categories" VALUES (9, 'Coffee', 1);
INSERT INTO "categories" VALUES (10, 'Juice', 1);
INSERT INTO "categories" VALUES (11, 'Soda', 1);
INSERT INTO "categories" VALUES (12, 'Tea', 1);
INSERT INTO "categories" VALUES (13, 'Water', 1);
INSERT INTO "categories" VALUES (14, 'Honey', 2);
INSERT INTO "categories" VALUES (15, 'Jam', 2);
INSERT INTO "categories" VALUES (16, 'Spices', 2);
INSERT INTO "categories" VALUES (17, 'Tomato_sauce', 2);
INSERT INTO "categories" VALUES (18, 'Vinegar', 2);
INSERT INTO "categories" VALUES (19, 'Milk', 3);
INSERT INTO "categories" VALUES (20, 'Oat-milk', 3);
INSERT INTO "categories" VALUES (21, 'Oatghurt', 3);
INSERT INTO "categories" VALUES (22, 'Sour-cream', 3);
INSERT INTO "categories" VALUES (23, 'Sour-milk', 3);
INSERT INTO "categories" VALUES (24, 'Soy-milk', 3);
INSERT INTO "categories" VALUES (25, 'Soyghurt', 3);
INSERT INTO "categories" VALUES (26, 'Yoghurt', 3);
INSERT INTO "categories" VALUES (27, 'Apple', 4);
INSERT INTO "categories" VALUES (28, 'Avocado', 4);
INSERT INTO "categories" VALUES (29, 'Banana', 4);
INSERT INTO "categories" VALUES (30, 'Kiwi', 4);
INSERT INTO "categories" VALUES (31, 'Lemon', 4);
INSERT INTO "categories" VALUES (32, 'Lime', 4);
INSERT INTO "categories" VALUES (33, 'Mango', 4);
INSERT INTO "categories" VALUES (34, 'Melon', 4);
INSERT INTO "categories" VALUES (35, 'Nectarine', 4);
INSERT INTO "categories" VALUES (36, 'Orange', 4);
INSERT INTO "categories" VALUES (37, 'Papaya', 4);
INSERT INTO "categories" VALUES (38, 'Passion-fruit', 4);
INSERT INTO "categories" VALUES (39, 'Peach', 4);
INSERT INTO "categories" VALUES (40, 'Pear', 4);
INSERT INTO "categories" VALUES (41, 'Pineapple', 4);
INSERT INTO "categories" VALUES (42, 'Plum', 4);
INSERT INTO "categories" VALUES (43, 'Pomegranate', 4);
INSERT INTO "categories" VALUES (44, 'Red-grapefruit', 4);
INSERT INTO "categories" VALUES (45, 'Satsumas', 4);
INSERT INTO "categories" VALUES (46, 'Fish', 5);
INSERT INTO "categories" VALUES (47, 'Nuts', 5);
INSERT INTO "categories" VALUES (48, 'Cake', 6);
INSERT INTO "categories" VALUES (49, 'Candy', 6);
INSERT INTO "categories" VALUES (50, 'Chips', 6);
INSERT INTO "categories" VALUES (51, 'Chocolate', 6);
INSERT INTO "categories" VALUES (52, 'Beans', 7);
INSERT INTO "categories" VALUES (53, 'Cereal', 7);
INSERT INTO "categories" VALUES (54, 'Flour', 7);
INSERT INTO "categories" VALUES (55, 'Oil', 7);
INSERT INTO "categories" VALUES (56, 'Pasta', 7);
INSERT INTO "categories" VALUES (57, 'Rice', 7);
INSERT INTO "categories" VALUES (58, 'Sugar', 7);
INSERT INTO "categories" VALUES (59, 'Asparagus', 8);
INSERT INTO "categories" VALUES (60, 'Aubergine', 8);
INSERT INTO "categories" VALUES (61, 'Brown-cap-mushroom', 8);
INSERT INTO "categories" VALUES (62, 'Cabbage', 8);
INSERT INTO "categories" VALUES (63, 'Carrots', 8);
INSERT INTO "categories" VALUES (64, 'Corn', 8);
INSERT INTO "categories" VALUES (65, 'Cucumber', 8);
INSERT INTO "categories" VALUES (66, 'Garlic', 8);
INSERT INTO "categories" VALUES (67, 'Ginger', 8);
INSERT INTO "categories" VALUES (68, 'Leek', 8);
INSERT INTO "categories" VALUES (69, 'Mushroom', 8);
INSERT INTO "categories" VALUES (70, 'Onion', 8);
INSERT INTO "categories" VALUES (71, 'Pepper', 8);
INSERT INTO "categories" VALUES (72, 'Potato', 8);
INSERT INTO "categories" VALUES (73, 'Red-beet', 8);
INSERT INTO "categories" VALUES (74, 'Tomato', 8);
INSERT INTO "categories" VALUES (75, 'Zucchini', 8);

CREATE TABLE "images" (
  "id" SERIAL PRIMARY KEY,
	"image_url" VARCHAR,
	"category_id" INT,
	"embedding" vector(512)
);
ALTER TABLE "images" ADD FOREIGN KEY ("category_id") REFERENCES "categories" ("id");

CREATE TABLE "items" (
  "id" SERIAL PRIMARY KEY,
  "user_id" INT NOT NULL,
  "name" VARCHAR NOT NULL,
	"description" TEXT,
  "category_id" INT,
	"image_id" INT,
  "expiry_date" DATE NOT NULL,
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

ALTER TABLE "items" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");
ALTER TABLE "items" ADD FOREIGN KEY ("category_id") REFERENCES "categories" ("id");
ALTER TABLE "items" ADD FOREIGN KEY ("image_id") REFERENCES "images" ("id");

CREATE TABLE "notification_types" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR NOT NULL,
  "description" TEXT
);

INSERT INTO "notification_types"(name, description) VALUES ('email', 'Send notification by email');
INSERT INTO "notification_types"(name, description) VALUES ('local notification', 'Send notification by local notification of user''s device');
INSERT INTO "notification_types"(name, description) VALUES ('both', 'Send notifiction by both methods');

CREATE TABLE "notifications" (
  "id" SERIAL PRIMARY KEY,
  "type_id" INT,
  "item_id" INT NOT NULL,
  "date" TIMESTAMP NOT NULL,
  "status" VARCHAR DEFAULT 'pending'
);

ALTER TABLE "notifications" ADD FOREIGN KEY ("type_id") REFERENCES "notification_types" ("id");

ALTER TABLE "notifications" ADD FOREIGN KEY ("item_id") REFERENCES "items" ("id");



CREATE TABLE "preferences" (
  "id" SERIAL PRIMARY KEY,
  "user_id" INT NOT NULL,
  "notification_days" INT NOT NULL DEFAULT 7,
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);
ALTER TABLE "preferences" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

CREATE TABLE "audit_logs" (
  "id" SERIAL PRIMARY KEY,
  "item_id" INT NOT NULL,
  "action" VARCHAR NOT NULL,
  "timestamp" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);
ALTER TABLE "audit_logs" ADD FOREIGN KEY ("item_id") REFERENCES "items" ("id");

CREATE TABLE "notification_settings" (
  "id" SERIAL PRIMARY KEY,
  "user_id" INT NOT NULL,
  "type_id" INT NOT NULL,
  "send_time" TIME,
  "enable_reminders" BOOL DEFAULT true
);
ALTER TABLE "notification_settings" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "notification_settings" ADD FOREIGN KEY ("type_id") REFERENCES "notification_types" ("id");

CREATE TABLE "item_history" (
  "id" SERIAL PRIMARY KEY,
  "item_id" INT NOT NULL,
  "action" VARCHAR NOT NULL,
  "action_date" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "previous_expiry_date" DATE,
  "new_expiry_date" DATE
);
ALTER TABLE "item_history" ADD FOREIGN KEY ("item_id") REFERENCES "items" ("id");

