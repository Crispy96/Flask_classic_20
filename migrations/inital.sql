CREATE TABLE "movimiento" (
	"id"	INTEGER,
	"fecha"	TEXT NOT NULL,
	"concepto"	TEXT NOT NULL,
	"ingreso_gasto"	TEXT NOT NULL,
	"cantidad"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)