--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11 (Homebrew)
-- Dumped by pg_dump version 14.11 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: movies; Type: TABLE; Schema: public; Owner: edward
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying(128),
    release_date date NOT NULL,
    end_date date
);


ALTER TABLE public.movies OWNER TO edward;

--
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: edward
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO edward;

--
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edward
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- Name: sales; Type: TABLE; Schema: public; Owner: edward
--

CREATE TABLE public.sales (
    id integer NOT NULL,
    movie_id integer,
    theater_id integer,
    sale_date date NOT NULL,
    total_sales numeric DEFAULT 0
);


ALTER TABLE public.sales OWNER TO edward;

--
-- Name: sales_id_seq; Type: SEQUENCE; Schema: public; Owner: edward
--

CREATE SEQUENCE public.sales_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sales_id_seq OWNER TO edward;

--
-- Name: sales_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edward
--

ALTER SEQUENCE public.sales_id_seq OWNED BY public.sales.id;


--
-- Name: theaters; Type: TABLE; Schema: public; Owner: edward
--

CREATE TABLE public.theaters (
    id integer NOT NULL,
    name character varying(128),
    city character varying(128)
);


ALTER TABLE public.theaters OWNER TO edward;

--
-- Name: theaters_id_seq; Type: SEQUENCE; Schema: public; Owner: edward
--

CREATE SEQUENCE public.theaters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.theaters_id_seq OWNER TO edward;

--
-- Name: theaters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edward
--

ALTER SEQUENCE public.theaters_id_seq OWNED BY public.theaters.id;


--
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: edward
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- Name: sales id; Type: DEFAULT; Schema: public; Owner: edward
--

ALTER TABLE ONLY public.sales ALTER COLUMN id SET DEFAULT nextval('public.sales_id_seq'::regclass);


--
-- Name: theaters id; Type: DEFAULT; Schema: public; Owner: edward
--

ALTER TABLE ONLY public.theaters ALTER COLUMN id SET DEFAULT nextval('public.theaters_id_seq'::regclass);


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: edward
--

COPY public.movies (id, title, release_date, end_date) FROM stdin;
1	Moana 2	2024-11-27	\N
2	Wicked	2024-11-22	\N
3	Red One	2024-11-15	\N
\.


--
-- Data for Name: sales; Type: TABLE DATA; Schema: public; Owner: edward
--

COPY public.sales (id, movie_id, theater_id, sale_date, total_sales) FROM stdin;
1	1	3	2024-11-30	11000
2	1	2	2024-11-30	12000
3	1	1	2024-11-30	13000
4	1	3	2024-11-29	12000
5	1	2	2024-11-29	13000
6	1	1	2024-11-29	14000
7	1	3	2024-11-28	5600
8	1	2	2024-11-28	6600
9	1	1	2024-11-28	7600
10	2	3	2024-11-30	6500
11	2	2	2024-11-30	7500
12	2	1	2024-11-30	8500
13	2	3	2024-11-29	7200
14	2	2	2024-11-29	8200
15	2	1	2024-11-29	9200
16	2	3	2024-11-28	3300
17	2	2	2024-11-28	4300
18	2	1	2024-11-28	5300
19	3	3	2024-11-30	420
20	3	2	2024-11-30	1420
21	3	1	2024-11-30	2420
22	3	3	2024-11-29	400
23	3	2	2024-11-29	1400
24	3	1	2024-11-29	2400
25	3	3	2024-11-28	100
26	3	2	2024-11-28	1000
27	3	1	2024-11-28	2000
\.


--
-- Data for Name: theaters; Type: TABLE DATA; Schema: public; Owner: edward
--

COPY public.theaters (id, name, city) FROM stdin;
1	AMC Saratoga 14	San Jose
2	Regal LA Live	Los Angeles
3	THE LOT Libert Station	San Diego
\.


--
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edward
--

SELECT pg_catalog.setval('public.movies_id_seq', 3, true);


--
-- Name: sales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edward
--

SELECT pg_catalog.setval('public.sales_id_seq', 27, true);


--
-- Name: theaters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edward
--

SELECT pg_catalog.setval('public.theaters_id_seq', 3, true);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: edward
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


--
-- Name: movies movies_title_key; Type: CONSTRAINT; Schema: public; Owner: edward
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_title_key UNIQUE (title);


--
-- Name: sales sales_pkey; Type: CONSTRAINT; Schema: public; Owner: edward
--

ALTER TABLE ONLY public.sales
    ADD CONSTRAINT sales_pkey PRIMARY KEY (id);


--
-- Name: theaters theaters_name_key; Type: CONSTRAINT; Schema: public; Owner: edward
--

ALTER TABLE ONLY public.theaters
    ADD CONSTRAINT theaters_name_key UNIQUE (name);


--
-- Name: theaters theaters_pkey; Type: CONSTRAINT; Schema: public; Owner: edward
--

ALTER TABLE ONLY public.theaters
    ADD CONSTRAINT theaters_pkey PRIMARY KEY (id);


--
-- Name: idx_sales_moid_sadate_totsa; Type: INDEX; Schema: public; Owner: edward
--

CREATE INDEX idx_sales_moid_sadate_totsa ON public.sales USING btree (movie_id, sale_date, total_sales);


--
-- Name: idx_sales_moid_thid_sadate; Type: INDEX; Schema: public; Owner: edward
--

CREATE UNIQUE INDEX idx_sales_moid_thid_sadate ON public.sales USING btree (movie_id, theater_id, sale_date);


--
-- Name: idx_sales_sadate; Type: INDEX; Schema: public; Owner: edward
--

CREATE INDEX idx_sales_sadate ON public.sales USING btree (sale_date);


--
-- Name: idx_sales_thid_sadate_totsa; Type: INDEX; Schema: public; Owner: edward
--

CREATE INDEX idx_sales_thid_sadate_totsa ON public.sales USING btree (theater_id, sale_date, total_sales);


--
-- Name: sales sales_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edward
--

ALTER TABLE ONLY public.sales
    ADD CONSTRAINT sales_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(id) ON DELETE CASCADE;


--
-- Name: sales sales_theater_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edward
--

ALTER TABLE ONLY public.sales
    ADD CONSTRAINT sales_theater_id_fkey FOREIGN KEY (theater_id) REFERENCES public.theaters(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

