# Proyecto Pizzas: Base de Datos

## Descripción
Este proyecto se centra en la creación y gestión de una base de datos para una pizzería, con el objetivo de manejar pedidos, clientes, y pizzas disponibles. Aunque inicialmente se planteó desarrollar una API, la fase actual del proyecto se ha concentrado en establecer una sólida base de datos que soporte las operaciones requeridas.

## Esquema de la Base de Datos
La base de datos está diseñada para almacenar información sobre clientes, pedidos y pizzas. A continuación, se describen las tablas principales y sus relaciones:

- **Clientes**: Almacena información de los clientes como ID, email y teléfono.
- **Pedidos**: Registra los pedidos realizados, incluyendo ID del pedido, fecha, hora, y la relación con el cliente que lo realiza.
- **Pizzas**: Contiene las pizzas disponibles, con campos para el nombre de la pizza y si está disponible o no.
- **Detalle de Pedidos**: Una tabla de relación que vincula los pedidos con las pizzas ordenadas, incluyendo la cantidad de cada pizza.

## Tecnologías Utilizadas
- **SQL**: Lenguaje utilizado para la creación y gestión de la base de datos.
- **SQLite/PostgreSQL**: Sistema de gestión de bases de datos. La elección depende del entorno de desarrollo y producción.

## Implementación
La implementación inicial se ha centrado en la creación de las tablas y relaciones necesarias para soportar las operaciones básicas de la pizzería. A continuación, se proporcionan los scripts SQL para crear las tablas mencionadas.

### Creación de Tablas
```sql
CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    telefono VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE Pizzas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) UNIQUE NOT NULL,
    disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE Pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fechaHora DATETIME NOT NULL,
    clienteId INTEGER,
    FOREIGN KEY (clienteId) REFERENCES Clientes(id)
);

CREATE TABLE DetallePedidos (
    pedidoId INTEGER,
    pizzaId INTEGER,
    cantidad INTEGER,
    FOREIGN KEY (pedidoId) REFERENCES Pedidos(id),
    FOREIGN KEY (pizzaId) REFERENCES Pizzas(id),
    PRIMARY KEY (pedidoId, pizzaId)
);

## Operaciones Básicas
Las operaciones básicas incluyen la inserción de datos en las tablas, la actualización de la disponibilidad de las pizzas, y la consulta de los pedidos y las pizzas más vendidas.

## Próximos Pasos
El siguiente paso en el desarrollo del proyecto es la implementación de una API que permita interactuar con la base de datos de manera programática, facilitando la realización de pedidos, la gestión de clientes y la consulta de información relevante a través de endpoints específicos.

## Reflexiones Finales
El enfoque inicial en la base de datos ha permitido establecer una fundación sólida para el proyecto. Aunque el desarrollo de la API está pendiente, la estructura actual de la base de datos está preparada para soportar las funcionalidades planeadas y futuras expansiones.

## Tiempo Invertido
El desarrollo de la base de datos y la documentación asociada ha tomado aproximadamente 9 horas, distribuidas a lo largo de un fin de semana. Este tiempo incluye la planificación, diseño del esquema de la base de datos, y la redacción de este documento.


