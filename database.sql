PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE roles (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO roles VALUES(1,'Admin');
INSERT INTO roles VALUES(2,'User');
CREATE TABLE genres (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO genres VALUES(1,'Fantazy');
INSERT INTO genres VALUES(2,'Science fiction');
INSERT INTO genres VALUES(5,'Romance');
INSERT INTO genres VALUES(6,'Children''s');
INSERT INTO genres VALUES(7,'Action');
INSERT INTO genres VALUES(8,'Comedy');
INSERT INTO genres VALUES(9,'Drama');
INSERT INTO genres VALUES(10,'Horror');
INSERT INTO genres VALUES(11,'Mystery');
INSERT INTO genres VALUES(12,'Thriller');
INSERT INTO genres VALUES(13,'Western');
INSERT INTO genres VALUES(14,'Historical fiction');
INSERT INTO genres VALUES(15,'Satire');
INSERT INTO genres VALUES(16,'Cyberpunk ');
INSERT INTO genres VALUES(17,'Speculative');
INSERT INTO genres VALUES(18,'Philosophy');
INSERT INTO genres VALUES(19,'Novel');
INSERT INTO genres VALUES(20,'Adventure');
INSERT INTO genres VALUES(21,'Poetry');
INSERT INTO genres VALUES(22,'Detective');
INSERT INTO genres VALUES(23,'Business');
INSERT INTO genres VALUES(24,'Psychology');
INSERT INTO genres VALUES(25,'Art and culture');
INSERT INTO genres VALUES(26,'Scientific literature');
INSERT INTO genres VALUES(27,'Computer literature');
INSERT INTO genres VALUES(28,'Medical literature');
CREATE TABLE users (
	id INTEGER NOT NULL, 
	email VARCHAR NOT NULL, 
	password VARCHAR NOT NULL, 
	username VARCHAR NOT NULL, 
	first_name VARCHAR, 
	last_name VARCHAR, 
	role_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(role_id) REFERENCES roles (id)
);
INSERT INTO users VALUES(1,'admin@bookstore.com','$2b$12$WXjdSpyAHKplKZXZw6GDZewKhk6vwRKUmHOvcV.rTCmmuMYB6pNN6','Admin',NULL,NULL,1);
INSERT INTO users VALUES(4,'rotor@gmail.com','$2b$12$OQq0P/2vpN/TBUKWLlAGVOBTLRoIQl/NCw4R3cMuNhLzKE2w1y2vy','rotor@gmail.com','rotor@gmail.com','rotor@gmail.com',1);
INSERT INTO users VALUES(5,'tester@test.com','$2b$12$i4n/C6g2ObFXxWbhXBZFfOUCjRqXetvEenEIvlWC0mAlez7kD6kqq','tester@test.com','tester@test.com','tester@test.com',2);
INSERT INTO users VALUES(6,'admin@gmail.com','$2b$12$GGb.mBgdfhsMFT9wFpRage6sdsovmocoWoPFJsj.pgxD8lwCMQa/W','admin@gmail.com','admin@gmail.com','admin@gmail.com',2);
CREATE TABLE books (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	author VARCHAR NOT NULL, 
	content VARCHAR, 
	price FLOAT NOT NULL, 
	publication_date DATETIME, 
	update_date DATETIME, 
	count INTEGER, 
	image VARCHAR, 
	"ISBN" VARCHAR NOT NULL, 
	owner_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owner_id) REFERENCES users (id)
);
INSERT INTO books VALUES(1,'1984','Джордж Оруэлл','«1984»  последняя книга Джорджа Оруэлла, он опубликовал ее в 1949 году, за год до смерти. Роман-антиутопия прославил автора и остается золотым стандартом жанра. Действие происходит в Лондоне, одном из главных городов тоталитарного супергосударства Океания. Пугающе детальное описание общества, основанного на страхе и угнетении, служит фоном для одной из самых ярких человеческих историй в мировой литературе. В центре сюжета судьба мелкого партийного функционера-диссидента Уинстона Смита и его опасный роман с коллегой. В СССР книга Оруэлла была запрещена до 1989 года: вероятно, партийное руководство страны узнавало в общественном строе Океании черты советской системы. Однако общество, описанное Оруэллом, не копия известных ему тоталитарных режимов. «1984» и сейчас читается как остроактуальный комментарий к текущим событиям.',12.990000000000000212,'2021-01-09 00:00:00.000000','2022-01-09 10:35:03.627133',1997,'08d746ce-7e88-44ef-9467-467e926e5066.jpg','978-617-7858-79-8',1);
INSERT INTO books VALUES(2,'Квадрант денежного потока ','Роберт Т. Кійосакі ','Автор цього супербестселеру, знаменитий Роберт Кійосакі, відповість вам, чому одні люди працюють менше, заробляють більше, платять менше податків і відчувають себе набагато більш захищеними у фінансовому відношенні, ніж інші. Ця книга допоможе вам знайти свій шлях до фінансової свободи в нашу еру великих змін.\n\n',15.990000000000000213,'2020-01-01 00:00:00.000000','2022-01-09 10:40:06.213449',100,'621772a7-3501-4259-86fe-5e59ca449615.jpg','978-985-15-4431-4',1);
INSERT INTO books VALUES(3,'Will','Марк Менсон, Вілл Сміт','Один із найдинамічніших і всесвітньовідомих акторів нашого часу розкриває усю правду про власне життя. У своїй сміливій і вражаючій книзі він говорить про свій непростий шлях до того місця, де поєднуються зовнішній успіх, внутрішнє щастя і єднання з людьми – він говорить про найдивовижний шлях у музиці й кінематографі, який будь-хто проходив.\n\n',17.989999999999998436,'2022-01-01 00:00:00.000000','2022-01-09 11:01:05.972782',199,'098f0dc1-dcd7-4864-866e-382c61add620.jpg','978-966-993-275-4',1);
INSERT INTO books VALUES(4,'Mythos. The Greek Myths Retold','Стівен Фрай','The Greek myths are amongst the best stories ever told, passed down through millennia and inspiring writers and artists as varied as Shakespeare, Michelangelo, James Joyce and Walt Disney. They are embedded deeply in the traditions, tales and cultural DNA of the West. You''ll fall in love with Zeus, marvel at the birth of Athena, wince at Cronus and Gaia''s revenge on Ouranos, weep with King Midas and hunt with the beautiful and ferocious Artemis. Spellbinding, informative and moving, Stephen Fry''s Mythos perfectly captures these stories for the modern age - in all their rich and deeply human relevance.\n\n',19.0,'2018-01-09 00:00:00.000000','2022-01-09 11:13:43.553929',50,'99881b88-6565-46cf-bd75-808c35ec2baf.jpg','9781405934138',1);
INSERT INTO books VALUES(5,'Атомні звички. Легкий і перевірений спосіб набути корисних звичок і позбутися звичок шкідливих','Джеймс Клір  ','Незначні зміни, значні результати! Дізнайтеся секрет тривалих результатів! Нашпигована заснованими на фактах стратегіями із самовдосконалення, книга «Атомні звички» навчить, як набути манер і навиків, що працюватимуть на вас, а не проти вас. У книзі Джеймс Клір ділиться надзвичайно цікавою і по-справжньому продуктивною методикою напрацювання корисних звичок. В її основі лежить поняття чотириступеневої моделі звичок (подразник, прагнення, відгук, винагорода), а також чотири породжені цією моделлю закони зміни поведінки. Викладений матеріал підтверджується результатами наукових досліджень, проте книгу слід трактувати не як наукову розвідку, а як посібник з експлуатації, що містить мудрі практичні поради та пояснення механізмів створення і змінювання власних звичок. Єдиного правильного способу набуття корисних звичок, звісно, не існує, але автор пропонує найкращий із відомих підхід, який спрацює незалежно від того, з чого саме ви починаєте і що саме намагаєтеся змінити. Викладені стратегії стануть у пригоді всім, хто потребує покрокової інструкції з покращення незалежно від того, що мається на меті — покращення здоров''я чи добробуту, продуктивності праці чи стосунків, а можливо, всього переліченого разом. Джеймс Клір — автор і лектор, який велику увагу приділяє таким питанням, як людські звички, механізм ухвалення рішень і методи постійного самовдосконалення. Його доробки друкувались у The New York Times, Entrepreneur, Time, а також були представлені глядачі американської ранкової телепрограми This Morning на CBS. Щомісяця веб-сайт Джеймса відвідують мільйони людей, а сотні тисяч підписані на його популярну електронну розсилку новин. Кліра як лектора постійно запрошують виступити компанії, що входять до списку Fortune 500, а його ідеї і напрацювання використовують члени команд Національної футбольної ліги, Національної баскетбольної асоціації і Головної ліги бейсболу. На його онлайн-курсі The Habits Academy пройшли навчання понад десять тисяч керівників, тренерів і вчителів. The Habits Academy — провідна освітня платформа, призначена як для приватних осіб, так і для працівників організацій, тобто усіх, хто прагне набути кращих звичок у побуті, особистій і професійній сферах.\n\n',8.9900000000000002131,'2021-11-25 00:00:00.000000','2022-01-09 11:26:08.261889',50,'834192cf-ec76-4406-ad63-9405a253d568.jpg','978-966-948-567-0',1);
INSERT INTO books VALUES(6,'The Lean Startup. How Constant Innovation Creates Radically Successful Businesses ','Ерік Райз ','Most new businesses fail. But most of those failures are preventable. The Lean Startup is the approach to business that''s being adopted around the world. It is changing the way companies are built and new products are launched. The Lean Startup is about learning what your customers really want. It''s about testing your vision continuously, adapting and adjusting before it''s too late. Now is the time to think Lean. The Lean Startup changes everything - Harvard Business Review\n',25.489999999999998435,'2011-02-23 00:00:00.000000','2022-01-09 11:30:55.912884',99,'f352a98d-8c6a-4e7c-a52e-d97309b80bd7.jpg','9780670921607',1);
INSERT INTO books VALUES(7,'The Lord of the Rings  ','Джон Р. Р. Толкін ','In ancient times the Rings of Power were crafted by the Elven-smiths, and Sauron, the Dark Lord, forged the One Ring, filling it with his own power so that he could rule the others. But the One Ring was taken from him, and though he sought it throughout Middle-earth still it remained lost to him. After many ages it fell, by chance, into the hands of the Hobbit, Bilbo Baggins. From his fastness in the Dark Tower of Mordor, Sauron''s power spread far and wide. He gathered all the Great Rings to him, but ever he searched for the One Ring that would complete his dominion. On his eleventy-first birthday, Bilbo disappeared, bequeathing to his young cousin, Frodo, the Ruling Ring, and a perilous quest: to journey across Middle-earth, deep into the shadow of the Dark Lord and destroy the Ring by casting it into the Cracks of Doom. "The Lord of the Rings" tells of the great quest undertaken by Frodo and the Fellowship of the Ring: Gandalf the wizard, Merry, Pippin and Sam, Gimli the Dwarf, Legolas the Elf, Boromir of Gondor, and a tall, mysterious stranger called Strider.\n',50.990000000000001989,'2004-11-25 00:00:00.000000','2022-01-09 11:44:41.595871',600,'67440324-73f7-42d2-8855-f8d25d2e3c9a.jpg','978-0-261-10320-7',1);
INSERT INTO books VALUES(8,'Чистий код. Створення і рефакторинг за допомогою Agile','Роберт Сесіл Мартін ','Навіть поганий програмний код може працювати. Однак якщо код не є «чистим», це завжди буде заважати розвитку проекту і компанії-розробника, віднімаючи значні ресурси на його підтримку і «приборкання». Ця книга присвячена хорошому програмуванню. У ній повно реальних прикладів коду. Прочитавши книгу, ви дізнаєтеся багато нового про коди. Більш того, ви навчитеся відрізняти хороший код від поганого. Ви дізнаєтеся, як писати хороший код і як перетворити поганий код у хороший.\n',25.989999999999998437,'2019-06-09 00:00:00.000000','2022-01-09 12:01:45.301306',86,'15dabdbf-f666-4a29-a5dc-726fa489fe32.png','978-617-09-5285-1',1);
INSERT INTO books VALUES(9,'Думай как математик. Как решать любые задачи быстрее и эффективнее ','Барбара Оклі ','Всі ми хочемо володіти високоінтелектуальним розумом, шикарною логікою, творчими здібностями, менше піддаватися прокрастинації. Книга «Думай як математик. Як вирішувати будь-які завдання швидше і ефективніше» присвячена саме тим питанням і труднощам, з якими доводиться стикатися на шляху до досконалості. Цінні поради та методики дають можливість переосмислити власне життя, вилучили зі звичної повсякденності максимальну користь. Існує думка, що люди математичного складу розуму в більшості не володіють яскравими інтелектуальними здібностями. Все це закладено генетично, і вимагає максимальної роботи над собою. Барбара Оаклі, докторка наук, доводить, що кожен може змінити спосіб свого мислення і оволодіти прийомами, які використовують всі фахівці з точних наук. Прочитавши цю книгу, Ви навчитеся: ефективно вирішувати завдання з будь-якої галузі знань; освоїте метод чергування різних типів завдань; навчитеся «стискати» ключові ідеї так, щоб їх було зручніше утримати в пам''яті, дізнаєтеся про можливості свого мозку дуже багато нового! Видання являє собою справжній підручник, тому читати його слід, озброївшись ручкою та зошитом для конспектів, щоб не упустити ніяких важливих дрібниць і домогтися найвищого результату в освоєнні нового. Унікальне творіння Барбари Оаклі буде просто незамінно і дуже корисно купити студентам будь-яких навчальних закладів, школярам, викладачам, батькам і всім, хто хоче зламати усталені стереотипи і в будь-якому віці освоїти потрібну йому сферу діяльності.\n',14.990000000000000213,'2018-06-14 00:00:00.000000','2022-01-09 12:08:24.284174',499,'e094292b-e259-40be-81da-44506e380fcc.jpg','978-5-9614-6624-9',1);
INSERT INTO books VALUES(10,'Все хреново. Книга о надежде','Марк Менсон ','Ніколи ще в історії людства ми не жили так добре: перемогли купу хвороб, отримали доступ до світових знань та оточили себе комфортом технологій. Однак чим кращим стає життя, тим більше ми турбуємося і переживаємо. Живемо з відчуттям, що все погано. Планета нагрівається, економічна нерівність зашкалює, політики крадуть і брешуть. Нашою невпевненістю в майбутньому, відчаєм і надією, що все буде нормально, вміло користуються всі кому не лінь - від маркетологів, які впарюють нам чергову непотрібну річ, до релігійних і політичних діячів. Що ж робити? Досить сподіватися на краще, каже Марк Менсон, автор світового бестселера «Тонке мистецтво пофігізму». У своїй новій книзі він розповідає про кризу надії, про марність віри в справедливий світ і про те, що якість нашого життя визначається якістю нашої особистості, а не тим, якими благами або негараздами обсипає нас світ. Спираючись на мудрість Ніцше і Канта, Платона і Тома Вейтса, автор допоможе вам виробити тверезий погляд на все, що вас оточує. Адже куди не глянь - всюди дійсно погано. Так було і буде завжди. Прийшов час перестати тікати від цієї істини і навчитися приймати життя як є.\n',12.990000000000000212,'2019-07-25 00:00:00.000000','2022-01-09 12:10:42.707056',79,'f8d27d23-3746-400d-9593-09b9fd55716c.jpg','978-617-7858-00-2',1);
INSERT INTO books VALUES(11,'100 рассказов из истории медицины','text','Перед вами історія доказової медицини XVI-XX ст., викладена у формі коротких ілюстрованих оповідей. У книзі описані як добре знайомі, так і абсолютно невідомі факти. Лікарі-дослідники, лікарі-новатори, лікарі-письменники, лікарі-пацієнти, лікарі-політики - всі вони здійснювали дивовижні відкриття і подвиги заради збереження життя пацієнтів. Ви дізнаєтеся про найбільш значущі операції, що поклали початок розвитку основних напрямків медицини; про те, як були відкриті збудники смертельних хвороб і про перемогу над ними; як розроблялися методи лікування хронічних захворювань і гострих станів; як винаходили і вдосконалювали медичну техніку і життєво важливі лікарські препарати. Автор доступно пояснює складні медичні терміни і суть важливих фізіологічних процесів. У книзі немає художнього вимислу: викладені факти підкріплені ретельною перевіркою в спеціальній літературі і періодиці, спогадах, інтерв''ю, лекціях, архівних матеріалах.\n',26.989999999999998436,'2019-06-09 00:00:00.000000','2022-01-10 16:34:40.927588',8,'fcd01e45-119f-4d26-9fee-b9689770bfa6.jpg','978-617-7858-05-7',1);
INSERT INTO books VALUES(12,'Поток. Психология оптимального переживания ','Мігай Чиксентмігаї ','text',17.989999999999998436,'2018-02-21 00:00:00.000000','2022-01-09 12:20:02.231493',40,'2e7f01a0-a7c7-4d96-9c10-d6867ec2f4d0.jpg','978-5-91671-857-7',1);
INSERT INTO books VALUES(13,'Думай і багатій','Наполеон Гілл','text',29.989999999999998436,'2017-07-09 00:00:00.000000','2022-01-09 12:23:25.760038',34,'f9f33e6b-7a4c-4e58-a76e-7e95bd0fb4be.jpeg','978-617-12-4120-6',1);
INSERT INTO books VALUES(14,'Brief History of Time','Стівен Гокінґ','Was there a beginning of time? Could time run backwards? Is the universe infinite or does it have boundaries? These are just some of the questions considered in an internationally acclaimed masterpiece by one of the world''s greatest thinkers. It begins by reviewing the great theories of the cosmos from Newton to Einstein, before delving into the secrets which still lie at the heart of space and time, from the Big Bang to black holes, via spiral galaxies and strong theory. To this day "A Brief History of Time" remains a staple of the scientific canon, and its succinct and clear language continues to introduce millions to the universe and its wonders.\n',40.990000000000001989,'2011-07-09 00:00:00.000000','2022-01-09 12:29:14.092831',59,'f64fa76a-f4fa-41fe-86f9-33b611e01b5f.jpg','9780857501004',1);
INSERT INTO books VALUES(15,'Кровь, пот и пиксели. Обратная сторона индустрии видеоигр','text','text',30.0,'2019-06-09 00:00:00.000000','2022-01-09 12:31:49.225262',288,'8ed6e7fc-9c6b-4fc4-bd7e-abe4e60f3587.jpg','978-617-7561-77-3',1);
INSERT INTO books VALUES(16,'Тореадори з Васюкiвки','Всеволод Нестайко','Важко знайти в нашій літературі щось настільки веселе, талановите й дотепне, як ця неперевершена книга Всеволода Нестайка, якого часто називають Гоголем сучасної української дитячої літератури. Недаремно «Тореадори з Васюківки» перекладено двадцятьма мовами і внесено до Особливо Почесного списку Андерсена як один з найвидатніших творів світової літератури для дітей. Це перше видання нової авторської редакції роману з новими надзвичайно веселими епізодами.',69000.0,'2004-01-27 00:00:00.000000','2022-01-10 15:05:43.048596',67,'9333ae7c-35df-4cbc-bcca-c2578761aa44.jpg','9789667047863',1);
INSERT INTO books VALUES(17,'Грокаем алгоритмы. Иллюстрированное пособие для программистов и любопытствующих','Адитья Бхаргава','О книге\n\nЯ (Адитья Бхаргава) прежде всего стремился к тому, чтобы книга легко читалась. Я избегаю неожиданных поворотов; каждый раз, когда в книге упоминается новая концепция, я либо объясняю ее сразу, либо говорю, где буду объяснять. Основные концепции подкрепляются упражнениями и повторными объяснениями, чтобы вы могли проверить свои предположения и убедиться в том, что не потеряли нить изложения.\n\nВ книге приводится множество примеров. Моя цель — не вывалить на читателя кучу невразумительных формул, а упростить наглядное представление этих концепций. Я также считаю, что мы лучше всего учимся тогда, когда можем вспомнить что-то уже известное, а примеры помогают освежить память. Так, когда вы вспоминаете, чем массивы отличаются от связанных списков (глава 2), просто вспомните, как ищете места для компании в кинотеатре. Наверное, вы уже поняли, что я сторонник визуального стиля обучения, — в книге полно рисунков.\n\nСодержимое книги было тщательно продумано. Нет смысла писать книгу с описанием всех алгоритмов сортировки — для этого есть такие источники, как Википедия и Khan Academy. Все алгоритмы, описанные в книге, имеют практическую ценность. Я применял их в своей работе программиста, и они закладывают хорошую основу для изучения более сложных тем.',10.990000000000000213,'2017-02-10 00:00:00.000000','2022-01-10 15:35:04.309684',198,'f42d6060-1095-448c-836c-65f0147f351d.jpg','978-5-496-02541-6',6);
CREATE TABLE orders (
	id INTEGER NOT NULL, 
	deliver_date DATETIME, 
	country VARCHAR, 
	city VARCHAR, 
	address VARCHAR, 
	user_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);
INSERT INTO orders VALUES(1,'2022-01-30 00:00:00.000000','Україна','Житомир','вул. Театральна, 9/5, Житомир, Житомирська область, 10004',5);
INSERT INTO orders VALUES(2,'2022-02-06 00:00:00.000000','Укріїна','Житомир','вул. Велика Бердичівська, 77',6);
INSERT INTO orders VALUES(3,'2022-01-20 00:00:00.000000','Ukraine','Zhytomyr','1243495',6);
INSERT INTO orders VALUES(4,'2022-02-04 00:00:00.000000','Украина','Zhytomyr','1243495',6);
CREATE TABLE books_genres (
	book_id INTEGER NOT NULL, 
	genre_id INTEGER NOT NULL, 
	PRIMARY KEY (book_id, genre_id), 
	FOREIGN KEY(book_id) REFERENCES books (id), 
	FOREIGN KEY(genre_id) REFERENCES genres (id)
);
INSERT INTO books_genres VALUES(16,9);
INSERT INTO books_genres VALUES(7,16);
INSERT INTO books_genres VALUES(16,8);
INSERT INTO books_genres VALUES(16,7);
INSERT INTO books_genres VALUES(1,19);
INSERT INTO books_genres VALUES(14,26);
INSERT INTO books_genres VALUES(4,25);
INSERT INTO books_genres VALUES(4,20);
INSERT INTO books_genres VALUES(4,14);
INSERT INTO books_genres VALUES(6,24);
INSERT INTO books_genres VALUES(7,20);
INSERT INTO books_genres VALUES(3,18);
INSERT INTO books_genres VALUES(3,24);
INSERT INTO books_genres VALUES(5,18);
INSERT INTO books_genres VALUES(5,25);
INSERT INTO books_genres VALUES(10,24);
INSERT INTO books_genres VALUES(17,27);
INSERT INTO books_genres VALUES(17,23);
INSERT INTO books_genres VALUES(9,26);
INSERT INTO books_genres VALUES(9,27);
INSERT INTO books_genres VALUES(13,23);
INSERT INTO books_genres VALUES(13,24);
INSERT INTO books_genres VALUES(2,23);
INSERT INTO books_genres VALUES(2,18);
INSERT INTO books_genres VALUES(15,27);
INSERT INTO books_genres VALUES(12,18);
INSERT INTO books_genres VALUES(12,24);
INSERT INTO books_genres VALUES(8,27);
INSERT INTO books_genres VALUES(8,25);
CREATE TABLE orders_books (
	id INTEGER NOT NULL, 
	count INTEGER, 
	consumer_id INTEGER, 
	order_id INTEGER, 
	book_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(consumer_id) REFERENCES users (id), 
	FOREIGN KEY(order_id) REFERENCES orders (id), 
	FOREIGN KEY(book_id) REFERENCES books (id)
);
INSERT INTO orders_books VALUES(1,2,5,1,8);
INSERT INTO orders_books VALUES(2,3,5,1,1);
INSERT INTO orders_books VALUES(4,1,6,2,10);
INSERT INTO orders_books VALUES(5,2,6,3,17);
INSERT INTO orders_books VALUES(6,1,6,3,9);
INSERT INTO orders_books VALUES(7,1,6,3,13);
INSERT INTO orders_books VALUES(8,1,6,3,3);
INSERT INTO orders_books VALUES(9,1,6,3,16);
INSERT INTO orders_books VALUES(10,12,6,3,8);
INSERT INTO orders_books VALUES(11,12,6,3,11);
INSERT INTO orders_books VALUES(12,12,6,3,15);
INSERT INTO orders_books VALUES(13,1,6,4,16);
CREATE UNIQUE INDEX ix_roles_name ON roles (name);
CREATE INDEX ix_roles_id ON roles (id);
CREATE INDEX ix_genres_id ON genres (id);
CREATE UNIQUE INDEX ix_genres_name ON genres (name);
CREATE INDEX ix_users_username ON users (username);
CREATE UNIQUE INDEX ix_users_email ON users (email);
CREATE INDEX ix_users_id ON users (id);
CREATE INDEX ix_books_id ON books (id);
CREATE UNIQUE INDEX "ix_books_ISBN" ON books ("ISBN");
CREATE INDEX ix_orders_id ON orders (id);
CREATE INDEX ix_orders_books_id ON orders_books (id);
COMMIT;
