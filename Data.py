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
		self.query = "SELECT id, username, password, nama, jabatan FROM data_manager"
		print('self.query : ', self.query)
		result = self.executeQuery(self.query, True)
		return result


class Karyawan(DataToko):
	
	def getDataKaryawan(self):
		self.query = "SELECT * FROM data_karyawan"
		print('self.query : ', self.query)
		result = self.executeQuery(self.query, True)
		return result

	def addDataKaryawan(self, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon):
		self.query = 'INSERT INTO data_karyawan (username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\',)' 
		self.query = self.query % (username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def updateDataKaryawan(self, id, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon):
		self.query = 'UPDATE data_karyawan SET username =\'%s\' password=\'%s\', nama_karyawan=\'%s\', jenis_kelamin=\'%s\', tanggal_lahir=\'%s\', alamat=\'%s\', no_telepon=\'%s\' WHERE id = %i;' 
		self.query = self.query % (username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon, id)
		print('self.query : ', self.query)
		self.executeQuery(self.query)

	def deleteDataKaryawan(self,id):
		self.query = 'DELETE FROM data_karyawan where id = %i' 
		self.query = self.query % (id)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
	

class Barang(DataToko):
	def getDataBarang(self):
		self.query = "SELECT id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang FROM data_barang"
		print('self.query : ', self.query)
		result = self.executeQuery(self.query, True)
		return result

	def addDataBarang(self, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
		self.query = 'INSERT INTO data_barang (no_barang, nama_barang, jenis_barang, harga_barang, stok_barang) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (no_barang, nama_barang, jenis_barang, harga_barang, stok_barang)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def updateDataBarang(self, id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
		self.query = "UPDATE data_barang SET no_barang = \'%s\', nama_barang = \'%s\', jenis_barang = \'%s\', harga_barang = \'%s\', stok_barang = \'%s\' WHERE id = %i"
		self.query = self.query % (no_barang, nama_barang, jenis_barang, harga_barang, stok_barang, id)
		print('self.query:',self.query)
		self.executeQuery(self.query)

	def deleteDataBarang(self,id):
		self.query = 'DELETE FROM data_barang where id = %i' 
		self.query = self.query % (id)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		



