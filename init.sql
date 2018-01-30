CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

DROP TABLE IF EXISTS "Data";
CREATE TABLE "Data" (
    "Metadata" jsonb  NULL DEFAULT '{}',
	"Image" BYTEA  NULL
);

DROP FUNCTION IF EXISTS "NotifyTrigger";
CREATE OR REPLACE FUNCTION "NotifyTrigger"() RETURNS trigger AS $$	
	BEGIN
        NOTIFY "TASK", 'Something' ;
	END;
$$ LANGUAGE plpgsql;


DROP TRIGGER IF EXISTS "onNewTask" on "Data";
CREATE TRIGGER "onNewTask" AFTER INSERT on "Data" FOR EACH ROW EXECUTE PROCEDURE "NotifyTrigger"();

