CREATE TABLE Logins (
    LogId INT AUTO_INCREMENT PRIMARY KEY,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE Funcionarios (
    Ci INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Apellido VARCHAR(255) NOT NULL,
    Fch_Nacimiento DATE NOT NULL,
    Dirección VARCHAR(255) NOT NULL,
    Teléfono VARCHAR(20) NOT NULL,
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
    Año INT NOT NULL,
    Semestre INT NOT NULL,
    Fch_Inicio DATE NOT NULL,
    Fch_Fin DATE NOT NULL
);

