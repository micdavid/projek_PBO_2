import sqlite3

class DataToko:

	def __init__(self):
		self.conn = sqlite3.connect("manajementoko.db")
		self.cursor = self.conn.cursor()

	def executeQuery(self, query, retVal=False):
		self.cursor.execute(query)
		all_results = self.cursor.fetchall()
		self.conn.commit()
		if retVal:
			return all_results


class Manager(DataToko):

	def getDataManager(self):
		self.query = "SELECT username, password FROM data_manager"
		print('self.query : ', self.query)
		result = self.executeQuery(self.query, True)
		return result


class Karyawan(DataToko):
	
	def getDataKaryawan(self):
		self.query = "SELECT id, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telphone FROM data_karyawan"
		print('self.query : ', self.query)
		result = self.executeQuery(self.query, True)
		return result

	def addDataKaryawan(self, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telephone):
		self.query = 'INSERT INTO data_karyawan (username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telephone) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\',)' 
		self.query = self.query % (username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telephone)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def updateKaryawan(self, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telephone, id):
		self.query = 'UPDATE data_karyawan SET username =\'%s\' password=\'%s\', nama_karyawan=\'%s\', jenis_kelamin=\'%s\', tanggal_lahir=\'%s\', alamat=\'%s\', no_telephone=\'%s\' where username = %i;' 
		self.query = self.query % (username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telephone, id)
		print('self.query : ', self.query)
		self.executeQuery(self.query)

	def deleteKaryawan(self,username):
		self.query = 'DELETE FROM data_karyawan where username = %i' 
		self.query = self.query % (username)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
	

class Barang(DataToko):
	def addDataBarang(self, id_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
		self.query = 'INSERT INTO data_barang (no_barang, nama_barang, jenis_barang, harga_barang, stok_barang) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (id_barang, nama_barang, jenis_barang, harga_barang, stok_barang)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDataBarang(self):
		self.query = "SELECT id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang FROM data_barang"
		print('self.query : ', self.query)
		result = self.executeQuery(self.query, True)
		return result

	def updateDataBarang(self, id_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
		self.query = 'UPDATE data_barang SET id_barang = ?, nama_barang = ?, jenis_barang = ?, harga_barang = ?, stok_barang = ?'
		self.query = self.query % (id_barang, nama_barang, jenis_barang, harga_barang, stok_barang)
		print('self.query:',self.query)
		self.executeQuery(self.query)

	def deleteBarang(self,id_barang):
		self.query = 'DELETE FROM data_barang where id_barang = %i' 
		self.query = self.query % (id_barang)
		print('self.query : ', self.query )
		self.executeQuery(self.query)

class Lapor(DataToko):
	def setDataLapor(self, id_laporan, no_barang, username):
		self.query = 'INSERT INTO data_laporan (id_laporan, no_barang, username) VALUES (\'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (id_laporan, no_barang, username)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDataLapor(self):
		self.query = "SELECT id_laporan, no_barang, username FROM data_laporan"
		print('self.query : ', self.query)
		result = self.executeQuery(self.query, True)
		return result

	def updateDataLapor(self, id_laporan, no_barang, username):
		self.query = 'UPDATE data_laporan SET id_laporan = ?, no_barang = ?, username = ?'
		self.query = self.query % (id_laporan, no_barang, username)
		print('self.query:',self.query)
		self.executeQuery(self.query)

	def deleteDataLapor(self,id_laporan):
		self.query = 'DELETE FROM data_laporan where id_laporan = %i' 
		self.query = self.query % (id_laporan)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		



