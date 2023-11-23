CREATE TABLE Logins (
    LogId VARCHAR(255) PRIMARY KEY,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE Funcionarios (
    Ci INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Apellido VARCHAR(255) NOT NULL,
    Fch_Nacimiento DATE NOT NULL,
    Direccion VARCHAR(255) NOT NULL,
    Telefono VARCHAR(20) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    LogId VARCHAR(255) NOT NULL,
    FOREIGN KEY (LogId) REFERENCES Logins(LogId)
);

CREATE TABLE Agenda (
    Nro INT AUTO_INCREMENT PRIMARY KEY,
    Ci INT NOT NULL,
    Fch_Agenda DATETIME NOT NULL,
    FOREIGN KEY (Ci) REFERENCES Funcionarios(Ci)
);

CREATE TABLE Carnet_Salud (
    Ci INT,
    Fch_Emision DATETIME NOT NULL,
    Fch_Vencimiento DATETIME,
    Comprobante MEDIUMBLOB NOT NULL,
    PRIMARY KEY (Ci)
    FOREIGN KEY (Ci) REFERENCES Funcionarios(Ci),
);

CREATE TABLE Periodos_Actualizacion (
    Anio INT NOT NULL,
    Semestre INT NOT NULL,
    Fch_Inicio DATE ,
    Fch_Fin DATE ,
    PRIMARY KEY (Fch_Inicio, Fch_Fin)
);
