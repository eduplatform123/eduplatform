-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 02, 2025 at 09:03 PM
-- Server version: 8.0.42
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `edu_platform`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Информация об университете', 7, 'add_universityinfo'),
(26, 'Can change Информация об университете', 7, 'change_universityinfo'),
(27, 'Can delete Информация об университете', 7, 'delete_universityinfo'),
(28, 'Can view Информация об университете', 7, 'view_universityinfo'),
(29, 'Can add Форма обратной связи', 8, 'add_feedbackform'),
(30, 'Can change Форма обратной связи', 8, 'change_feedbackform'),
(31, 'Can delete Форма обратной связи', 8, 'delete_feedbackform'),
(32, 'Can view Форма обратной связи', 8, 'view_feedbackform'),
(33, 'Can add Вложение к обратной связи', 9, 'add_feedbackattachment'),
(34, 'Can change Вложение к обратной связи', 9, 'change_feedbackattachment'),
(35, 'Can delete Вложение к обратной связи', 9, 'delete_feedbackattachment'),
(36, 'Can view Вложение к обратной связи', 9, 'view_feedbackattachment'),
(37, 'Can add Профиль пользователя', 10, 'add_userprofile'),
(38, 'Can change Профиль пользователя', 10, 'change_userprofile'),
(39, 'Can delete Профиль пользователя', 10, 'delete_userprofile'),
(40, 'Can view Профиль пользователя', 10, 'view_userprofile'),
(41, 'Can add Публичная обратная связь', 11, 'add_publicfeedback'),
(42, 'Can change Публичная обратная связь', 11, 'change_publicfeedback'),
(43, 'Can delete Публичная обратная связь', 11, 'delete_publicfeedback'),
(44, 'Can view Публичная обратная связь', 11, 'view_publicfeedback'),
(45, 'Can add Новость/Статья', 12, 'add_newsarticle'),
(46, 'Can change Новость/Статья', 12, 'change_newsarticle'),
(47, 'Can delete Новость/Статья', 12, 'delete_newsarticle'),
(48, 'Can view Новость/Статья', 12, 'view_newsarticle');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$1000000$ALZtVuP4KIIoOMaBhbmBbd$d3oaE5Nwu6gh/2B40gnid0PyVMXGOd2b43MPzeLtaMw=', '2025-09-01 11:50:10.919908', 0, 'dima', '', '', 'dima@gmail.com', 0, 1, '2025-08-31 09:52:48.472252'),
(2, 'pbkdf2_sha256$1000000$PWE8rmpOqkoXETAftqhzab$4VDIwSHP4Sn2koVZdt67lH6flA7JiMyV7HXWPiZP0/g=', '2025-09-03 10:58:34.318282', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2025-08-31 09:57:18.572581'),
(3, 'pbkdf2_sha256$1000000$T4zWmzXoUfHy89H9vPoCx0$EodS9ChVkwAm6xVkxsHlajqIlTRJ89ocjuc3jX2JORk=', '2025-09-01 11:48:39.412502', 0, 'vasiliy', '', '', 'vasya@gmail.com', 0, 1, '2025-08-31 10:38:57.966309');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'main', 'feedbackattachment'),
(8, 'main', 'feedbackform'),
(12, 'main', 'newsarticle'),
(11, 'main', 'publicfeedback'),
(7, 'main', 'universityinfo'),
(10, 'main', 'userprofile'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-08-31 09:05:12.421857'),
(2, 'auth', '0001_initial', '2025-08-31 09:05:13.259680'),
(3, 'admin', '0001_initial', '2025-08-31 09:05:13.439006'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-08-31 09:05:13.452821'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-08-31 09:05:13.464103'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-08-31 09:05:13.594976'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-08-31 09:05:13.697338'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-08-31 09:05:13.780223'),
(9, 'auth', '0004_alter_user_username_opts', '2025-08-31 09:05:13.788943'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-08-31 09:05:13.863234'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-08-31 09:05:13.867232'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-08-31 09:05:13.876125'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-08-31 09:05:13.968055'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-08-31 09:05:14.064143'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-08-31 09:05:14.147521'),
(16, 'auth', '0011_update_proxy_permissions', '2025-08-31 09:05:14.157821'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-08-31 09:05:14.260457'),
(18, 'main', '0001_initial', '2025-08-31 09:05:14.699943'),
(19, 'sessions', '0001_initial', '2025-08-31 09:05:14.751882'),
(20, 'main', '0002_remove_userprofile_department_and_more', '2025-08-31 09:42:06.498627'),
(21, 'main', '0003_publicfeedback', '2025-08-31 11:36:02.166437'),
(22, 'main', '0004_newsarticle', '2025-08-31 16:05:53.520700');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('zn9pc5tec7bfujf5lp965z7nhma7juh8', '.eJxVjEsOAiEQBe_C2hChm48u3XsG0tAgowaSYWZlvLtOMgvdvqp6LxFoXWpYR57DxOIstDj8bpHSI7cN8J3arcvU2zJPUW6K3OmQ1875edndv4NKo35rb5NOmpwyhgDYcaFkbCZ0JdoTOgb0FGOBglk5RqtYMYL2YN0xAYn3B_DqN_8:1uthRy:13tU1lsLV8ADDMIXX07JCk-8RgE6s0KJvmOA7hJ6U0A', '2025-09-17 10:58:34.338132');

-- --------------------------------------------------------

--
-- Table structure for table `main_feedbackattachment`
--

CREATE TABLE `main_feedbackattachment` (
  `id` bigint NOT NULL,
  `file` varchar(100) NOT NULL,
  `filename` varchar(255) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `feedback_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `main_feedbackattachment`
--

INSERT INTO `main_feedbackattachment` (`id`, `file`, `filename`, `uploaded_at`, `feedback_id`) VALUES
(1, 'feedback_attachments/test.docx', 'test.docx', '2025-08-31 10:43:01.095084', 1);

-- --------------------------------------------------------

--
-- Table structure for table `main_feedbackform`
--

CREATE TABLE `main_feedbackform` (
  `id` bigint NOT NULL,
  `subject` varchar(200) NOT NULL,
  `message` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `teacher_response` longtext,
  `response_date` datetime(6) DEFAULT NULL,
  `student_id` int NOT NULL,
  `teacher_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `main_feedbackform`
--

INSERT INTO `main_feedbackform` (`id`, `subject`, `message`, `status`, `created_at`, `updated_at`, `teacher_response`, `response_date`, `student_id`, `teacher_id`) VALUES
(1, 'Test', 'Testsetdlfg', 'pending', '2025-08-31 10:43:01.081636', '2025-08-31 10:43:01.081636', NULL, NULL, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `main_newsarticle`
--

CREATE TABLE `main_newsarticle` (
  `id` bigint NOT NULL,
  `title` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `excerpt` longtext NOT NULL,
  `category` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `featured_image` varchar(100) DEFAULT NULL,
  `tags` varchar(200) NOT NULL,
  `views_count` int UNSIGNED NOT NULL,
  `is_featured` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `published_at` datetime(6) DEFAULT NULL,
  `author_id` int NOT NULL
) ;

--
-- Dumping data for table `main_newsarticle`
--

INSERT INTO `main_newsarticle` (`id`, `title`, `slug`, `content`, `excerpt`, `category`, `status`, `featured_image`, `tags`, `views_count`, `is_featured`, `created_at`, `updated_at`, `published_at`, `author_id`) VALUES
(1, 'Открытие нового компьютерного класса', 'otkrytie-novogo-kompyuternogo-klassa', '<h2>Современные технологии для студентов</h2>\r\n            \r\n            <p>Мы рады сообщить о торжественном открытии нового компьютерного класса, оснащенного современным оборудованием. Класс включает в себя 25 рабочих мест с мощными компьютерами, интерактивную доску и проекционное оборудование.</p>\r\n            \r\n            <h3>Что нового:</h3>\r\n            <ul>\r\n                <li>25 современных компьютеров с последними процессорами</li>\r\n                <li>Интерактивная доска для презентаций</li>\r\n                <li>Высокоскоростной интернет</li>\r\n                <li>Специализированное программное обеспечение</li>\r\n                <li>Комфортная мебель и освещение</li>\r\n            </ul>\r\n            \r\n            <p>Новый компьютерный класс будет использоваться для проведения занятий по информатике, программированию, дизайну и другим техническим дисциплинам. Студенты смогут работать с современным программным обеспечением и развивать практические навыки.</p>\r\n            \r\n            <h3>Расписание работы:</h3>\r\n            <p>Понедельник - Пятница: 9:00 - 21:00<br>\r\n            Суббота: 10:00 - 18:00<br>\r\n            Воскресенье: выходной</p>\r\n            \r\n            <p>Записаться на занятия можно у кураторов групп или в деканате факультета.</p>', 'Торжественное открытие нового компьютерного класса с современным оборудованием для студентов технических специальностей.', 'news', 'published', 'news_images/comp_lab.jpg', 'компьютерный класс, технологии, образование, студенты', 2, 1, '2025-08-31 16:15:24.411502', '2025-09-03 10:59:34.257324', '2025-08-31 16:15:24.411502', 2),
(2, 'Международная конференция по искусственному интеллекту', 'mezhdunarodnaya-konferentsiya-po-iskusstvennomu-intellektu', '\n            <h2>Будущее технологий уже здесь</h2>\n            \n            <p>15-17 марта 2024 года в нашем университете состоится международная конференция \"Искусственный интеллект в современном мире: вызовы и возможности\". Мероприятие соберет ведущих экспертов в области ИИ из России, Европы и США.</p>\n            \n            <h3>Программа конференции:</h3>\n            \n            <h4>День 1 (15 марта):</h4>\n            <ul>\n                <li>09:00 - Регистрация участников</li>\n                <li>10:00 - Открытие конференции</li>\n                <li>11:00 - Пленарное заседание \"Современные тенденции в ИИ\"</li>\n                <li>14:00 - Секция \"Машинное обучение\"</li>\n                <li>16:00 - Секция \"Нейронные сети\"</li>\n            </ul>\n            \n            <h4>День 2 (16 марта):</h4>\n            <ul>\n                <li>10:00 - Секция \"Компьютерное зрение\"</li>\n                <li>12:00 - Мастер-класс \"Практическое применение ИИ\"</li>\n                <li>14:00 - Секция \"Этика ИИ\"</li>\n                <li>16:00 - Круглый стол \"Будущее образования в эпоху ИИ\"</li>\n            </ul>\n            \n            <h4>День 3 (17 марта):</h4>\n            <ul>\n                <li>10:00 - Презентация студенческих проектов</li>\n                <li>12:00 - Закрытие конференции</li>\n                <li>14:00 - Неформальное общение и нетворкинг</li>\n            </ul>\n            \n            <h3>Участие:</h3>\n            <p>Для участия в конференции необходимо зарегистрироваться на сайте университета до 10 марта 2024 года. Участие бесплатное для студентов и преподавателей университета.</p>\n            \n            <p>По всем вопросам обращайтесь в оргкомитет конференции: ai-conference@university.edu</p>\n            ', 'Международная конференция по искусственному интеллекту соберет ведущих экспертов для обсуждения современных технологий и их влияния на образование.', 'event', 'published', '', 'искусственный интеллект, конференция, технологии, образование', 1, 1, '2025-08-31 16:15:24.416475', '2025-08-31 16:15:24.416475', '2025-08-31 16:15:24.416475', 2),
(3, 'Советы по подготовке к экзаменам от преподавателей', 'sovety-po-podgotovke-k-ekzamenam-ot-prepodavateley', '<h2>Как эффективно подготовиться к сессии</h2>\r\n            \r\n            <p>Приближается экзаменационная сессия, и мы подготовили для вас полезные советы от наших опытных преподавателей, которые помогут успешно сдать все экзамены.</p>\r\n            \r\n            <h3>Советы по организации времени:</h3>\r\n            \r\n            <h4>1. Составьте план подготовки</h4>\r\n            <p>Разделите материал на логические блоки и распределите время на изучение каждого. Начните с самых сложных тем, оставив легкие на конец.</p>\r\n            \r\n            <h4>2. Используйте технику \"Помодоро\"</h4>\r\n            <p>Занимайтесь по 25 минут с перерывами по 5 минут. После 4 циклов делайте длинный перерыв 15-20 минут.</p>\r\n            \r\n            <h4>3. Чередуйте предметы</h4>\r\n            <p>Не зацикливайтесь на одном предмете весь день. Переключайтесь между разными дисциплинами для лучшего усвоения материала.</p>\r\n            \r\n            <h3>Методы запоминания:</h3>\r\n            \r\n            <h4>1. Конспектирование</h4>\r\n            <p>Пишите краткие конспекты своими словами. Это помогает лучше понять и запомнить материал.</p>\r\n            \r\n            <h4>2. Ментальные карты</h4>\r\n            <p>Создавайте визуальные схемы связей между понятиями. Это особенно эффективно для гуманитарных наук.</p>\r\n            \r\n            <h4>3. Повторение</h4>\r\n            <p>Повторяйте материал через определенные интервалы: сразу после изучения, через день, через неделю.</p>\r\n            \r\n            <h3>Психологическая подготовка:</h3>\r\n            \r\n            <h4>1. Полноценный сон</h4>\r\n            <p>Спите не менее 7-8 часов в сутки. Недостаток сна снижает способность к концентрации и запоминанию.</p>\r\n            \r\n            <h4>2. Физическая активность</h4>\r\n            <p>Делайте перерывы для легкой физической разминки. Это улучшает кровообращение и работу мозга.</p>\r\n            \r\n            <h4>3. Правильное питание</h4>\r\n            <p>Ешьте продукты, богатые омега-3 жирными кислотами, витаминами группы B и антиоксидантами.</p>\r\n            \r\n            <h3>В день экзамена:</h3>\r\n            <ul>\r\n                <li>Хорошо выспитесь</li>\r\n                <li>Позавтракайте</li>\r\n                <li>Придите заранее</li>\r\n                <li>Дышите глубоко и спокойно</li>\r\n                <li>Внимательно читайте вопросы</li>\r\n                <li>Начинайте с легких вопросов</li>\r\n            </ul>\r\n            \r\n            <p>Помните: подготовка к экзаменам - это марафон, а не спринт. Начинайте готовиться заранее, и у вас все получится!</p>\r\n            \r\n            <p><strong>Удачи на экзаменах!</strong></p>', 'Полезные советы от преподавателей университета по эффективной подготовке к экзаменационной сессии и успешной сдаче экзаменов.', 'blog', 'published', 'news_images/exam.jpg', 'экзамены, подготовка, советы, образование, студенты', 4, 0, '2025-08-31 16:15:24.421206', '2025-09-03 10:58:45.711324', '2025-08-31 16:15:24.421206', 2);

-- --------------------------------------------------------

--
-- Table structure for table `main_publicfeedback`
--

CREATE TABLE `main_publicfeedback` (
  `id` bigint NOT NULL,
  `name` varchar(100) NOT NULL,
  `theme` varchar(200) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `message` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `main_publicfeedback`
--

INSERT INTO `main_publicfeedback` (`id`, `name`, `theme`, `phone`, `message`, `status`, `created_at`, `updated_at`) VALUES
(1, 'test', 'test', '8134579', 'etihskdjg', 'completed', '2025-08-31 11:38:49.414817', '2025-08-31 11:44:22.085204');

-- --------------------------------------------------------

--
-- Table structure for table `main_universityinfo`
--

CREATE TABLE `main_universityinfo` (
  `id` bigint NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `page_type` varchar(50) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `main_userprofile`
--

CREATE TABLE `main_userprofile` (
  `id` bigint NOT NULL,
  `user_type` varchar(10) NOT NULL,
  `student_id` varchar(20) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `main_userprofile`
--

INSERT INTO `main_userprofile` (`id`, `user_type`, `student_id`, `created_at`, `updated_at`, `user_id`) VALUES
(1, 'student', '124667', '2025-08-31 09:52:49.151124', '2025-09-01 11:50:10.923513', 1),
(2, 'admin', NULL, '2025-08-31 10:04:54.414541', '2025-09-03 10:58:34.334415', 2),
(3, 'teacher', NULL, '2025-08-31 10:38:58.579982', '2025-09-01 11:48:39.416500', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `main_feedbackattachment`
--
ALTER TABLE `main_feedbackattachment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_feedbackattachm_feedback_id_22d7a66a_fk_main_feed` (`feedback_id`);

--
-- Indexes for table `main_feedbackform`
--
ALTER TABLE `main_feedbackform`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_feedbackform_student_id_21c63864_fk_auth_user_id` (`student_id`),
  ADD KEY `main_feedbackform_teacher_id_55bedc04_fk_auth_user_id` (`teacher_id`);

--
-- Indexes for table `main_newsarticle`
--
ALTER TABLE `main_newsarticle`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `main_newsarticle_author_id_3109fa14_fk_auth_user_id` (`author_id`);

--
-- Indexes for table `main_publicfeedback`
--
ALTER TABLE `main_publicfeedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `main_universityinfo`
--
ALTER TABLE `main_universityinfo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `main_userprofile`
--
ALTER TABLE `main_userprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `main_feedbackattachment`
--
ALTER TABLE `main_feedbackattachment`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `main_feedbackform`
--
ALTER TABLE `main_feedbackform`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `main_newsarticle`
--
ALTER TABLE `main_newsarticle`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_publicfeedback`
--
ALTER TABLE `main_publicfeedback`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `main_universityinfo`
--
ALTER TABLE `main_universityinfo`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_userprofile`
--
ALTER TABLE `main_userprofile`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `main_feedbackattachment`
--
ALTER TABLE `main_feedbackattachment`
  ADD CONSTRAINT `main_feedbackattachm_feedback_id_22d7a66a_fk_main_feed` FOREIGN KEY (`feedback_id`) REFERENCES `main_feedbackform` (`id`);

--
-- Constraints for table `main_feedbackform`
--
ALTER TABLE `main_feedbackform`
  ADD CONSTRAINT `main_feedbackform_student_id_21c63864_fk_auth_user_id` FOREIGN KEY (`student_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `main_feedbackform_teacher_id_55bedc04_fk_auth_user_id` FOREIGN KEY (`teacher_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `main_newsarticle`
--
ALTER TABLE `main_newsarticle`
  ADD CONSTRAINT `main_newsarticle_author_id_3109fa14_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `main_userprofile`
--
ALTER TABLE `main_userprofile`
  ADD CONSTRAINT `main_userprofile_user_id_15c416f4_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
