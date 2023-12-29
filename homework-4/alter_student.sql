-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar

CREATE TABLE students
( student_id serial,
 first_name varchar,
 last_name varchar,
 birthday date,
 phone varchar
);

-- 2. Добавить в таблицу student колонку middle_name varchar

ALTER TABLE students ADD COLUMN middle_name varchar;

-- 3. Удалить колонку middle_name

ALTER TABLE students DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date

ALTER TABLE students RENAME  birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)

ALTER TABLE students ALTER COLUMN phone SET DATA TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора

ALTER TABLE students ALTER COLUMN student_id SET DEFAULT nextval('students_student_id_seq');

-- ИЛИ

ALTER TABLE students ADD CONSTRAINT pk_students_students_id PRIMARY KEY(student_id)


INSERT INTO students(first_name, last_name, birth_date, phone) VALUES
('John', 'Smith', '13.03.1990', '788890830302'),
('Mark', 'Peach', '16.12.1989', '788689858798'),
('Mary', 'Scramble', '24.06.1993', '897987897903')


-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние

TRUNCATE TABLE students RESTART IDENTITY;