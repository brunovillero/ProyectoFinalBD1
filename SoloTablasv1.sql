CREATE TABLE Logins (
    LogId INT AUTO_INCREMENT PRIMARY KEY,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE Funcionarios (
    Ci INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Apellido VARCHAR(255) NOT NULL,
    Fch_Nacimiento DATE NOT NULL,
    Direccion VARCHAR(255) NOT NULL,
    Telefono VARCHAR(20) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    LogId INT NOT NULL,
    FOREIGN KEY (LogId) REFERENCES Logins(LogId)
);

CREATE TABLE Agenda (
    Nro INT AUTO_INCREMENT PRIMARY KEY,
    Ci INT NOT NULL,
    Fch_Agenda DATETIME NOT NULL,
    FOREIGN KEY (Ci) REFERENCES Funcionarios(Ci)
);

CREATE TABLE Carnet_Salud (
    Ci INT NOT NULL,
    Fch_Emision DATETIME NOT NULL,
    Fch_Vencimiento DATETIME NOT NULL,
    Comprobante MEDIUMBLOB NOT NULL,
    FOREIGN KEY (Ci) REFERENCES Funcionarios(Ci)
);

CREATE TABLE Periodos_Actualizacion (
    Ano INT NOT NULL,
    Semestre INT NOT NULL,
    Fch_Inicio DATE NOT NULL,
    Fch_Fin DATE NOT NULL
);


-- Primera Persona
INSERT INTO Logins (Password) VALUES ('password123');
SET @last_log_id1 = LAST_INSERT_ID();
INSERT INTO Funcionarios (Ci, Nombre, Apellido, Fch_Nacimiento, Direccion, Telefono, Email, LogId)
VALUES (12345678, 'Juan', 'Pérez', '1990-01-01', 'Calle Falsa 123', '0991234567', 'juan@example.com', @last_log_id1);

-- Segunda Persona
INSERT INTO Logins (Password) VALUES ('password456');
SET @last_log_id2 = LAST_INSERT_ID();
INSERT INTO Funcionarios (Ci, Nombre, Apellido, Fch_Nacimiento, Direccion, Telefono, Email, LogId)
VALUES (23456789, 'Maria', 'Lopez', '1992-02-02', 'Avenida Siempre Viva 456', '0997654321', 'maria@example.com', @last_log_id2);

-- Tercera Persona
INSERT INTO Logins (Password) VALUES ('password789');
SET @last_log_id3 = LAST_INSERT_ID();
INSERT INTO Funcionarios (Ci, Nombre, Apellido, Fch_Nacimiento, Direccion, Telefono, Email, LogId)
VALUES (34567890, 'Carlos', 'Garcia', '1994-03-03', 'Ruta 789 Km 10', '0981231234', 'carlos@example.com', @last_log_id3);





