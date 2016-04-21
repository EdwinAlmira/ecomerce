DELIMITER $$
 CREATE TRIGGER borrar_usuario AFTER DELETE ON login_personaladministrativo
	FOR EACH ROW BEGIN 
		delete from  login_myuser where id_user=old.id;
END $$