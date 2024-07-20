import pymysql
import config

db = cursor = None

class MPeserta:
    def __init__(self, idpeserta=None, namalengkap=None, nik=None, email=None, nowa=None, program=None):
        self.idpeserta = idpeserta
        self.namalengkap = namalengkap
        self.nik = nik
        self.email = nowa
        self.program = program
    def openDB(self):
        global db, cursor
        db = pymysql.connect(
                host=config.DB_HOST,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                database=config.DB_NAME)
        cursor = db.cursor()
           
    def closeDB(self):
        global db, cursor
        db.close()
    
    def selectDB(self):
        self.openDB()
        cursor.execute("SELECT * FROM peserta")
        container = [] 
        for idpeserta, namalengkap, nik, email, nowa, program in cursor.fetchall():
            container.append((idpeserta, namalengkap, nik, email, nowa, program))
        self.closeDB()
        return container
    
    def insertDB(self, data):
        self.openDB()
        cursor.execute("INSERT INTO peserta (namalengkap, nik, email, nowa, program) VALUES('%s', '%s', '%s', '%s', '%s')" % data)
        db.commit()
        self.closeDB()
    
    def getDBbyNo(self, idpeserta):
        self.openDB ()
        cursor.execute("SELECT * FROM peserta WHERE idpeserta='%s'" % idpeserta)
        data = cursor.fetchone()
        return data

    def updateDB(self, data):
        self.openDB()
        cursor.execute("UPDATE peserta SET namalengkap='%s', nik='%s', email='%s', nowa='%s', program='%s' WHERE idpeserta=%s" % data)
        db.commit()
        self.closeDB()

    def deleteDB (self, no):
        self.openDB ()
        cursor.execute("DELETE FROM peserta WHERE idpeserta=%s" % no)
        db.commit()
        self.closeDB()
		
	# def getProg(self):
		# self.openDB()
		# cursor.execute("SELECT * FROM program")
		# container = []
		# for idprogram, program, gambar, deskripsi in cursor.fetchall():
			# container.append((idprogram, program, gambar, deskripsi))
		# self.closeDB()
		# return container