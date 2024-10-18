SQL
CREATE TABLE temas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE questoes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    pergunta TEXT,
    alternativas JSON,
    resposta_correta INT,
    tema_id INT,
    FOREIGN KEY (tema_id) REFERENCES temas(id)
);