-- Table: public.api_employee

DROP TABLE IF EXISTS public.api_employee;
DROP INDEX IF EXISTS public.api_employee_category_id_8a6da679;
DROP INDEX IF EXISTS public.api_employee_position_id_52ce9e36;

CREATE TABLE IF NOT EXISTS public.api_employee
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY,
    "fullName" character varying(255) COLLATE pg_catalog."default" NOT NULL,
    "isMan" boolean NOT NULL,
    "birthDay" timestamp with time zone NOT NULL,
    category_id integer NOT NULL,
    position_id integer NOT NULL,
    CONSTRAINT api_employee_pkey PRIMARY KEY (id),
    CONSTRAINT "api_employee_category_id_8a6da679_fk_api_сategory_id" FOREIGN KEY (category_id)
        REFERENCES public."api_сategory" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT api_employee_position_id_52ce9e36_fk_api_position_id FOREIGN KEY (position_id)
        REFERENCES public.api_position (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.api_employee
    OWNER to postgres;

GRANT ALL ON TABLE public.api_employee TO postgres;
-- Index: api_employee_category_id_8a6da679


CREATE INDEX IF NOT EXISTS api_employee_category_id_8a6da679
    ON public.api_employee USING btree
    (category_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: api_employee_position_id_52ce9e36


CREATE INDEX IF NOT EXISTS api_employee_position_id_52ce9e36
    ON public.api_employee USING btree
    (position_id ASC NULLS LAST)
    TABLESPACE pg_default;


-- Table: public.api_position

DROP TABLE IF EXISTS public.api_position;

CREATE TABLE IF NOT EXISTS public.api_position
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY,
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "isActive" boolean NOT NULL,
    "isDeleted" boolean NOT NULL,
    CONSTRAINT api_position_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.api_position
    OWNER to postgres;

GRANT ALL ON TABLE public.api_position TO postgres;

-- Table: public.api_сategory

DROP TABLE IF EXISTS public."api_сategory";

CREATE TABLE IF NOT EXISTS public."api_сategory"
(
    id integer NOT NULL DEFAULT nextval('"api_сategory_id_seq"'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "api_сategory_pkey" PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."api_сategory"
    OWNER to postgres;

GRANT ALL ON TABLE public."api_сategory" TO postgres;