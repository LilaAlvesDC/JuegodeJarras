# Juego de Jarras

## Estructuras de Datos

Cuando hablamos a estructura de Datos nos referimos a cómo organizamos los datos cuando programamos. Básicamente, este tema trata de encontrar formas particulares de  organizar datos de tal manera que puedan ser utilizados de manera eficiente.

Imaginen que los datos que tenemos que manejar son libros!, y en un principio tenemos muchísimos libros desordenados por casa. Cada vez que queremos leer un libro, tardamos dos horas buscando uno por uno hasta dar con el libro. Eso no es eficiente. Entonces, ¿qué hacemos? Bueno, podemos armar una biblioteca, por ejemplo, y acomodamos los libros en orden alfabético, esto nos ahorra tiempo en buscarlos. Y, ¿qué pasa si tenemos demasiados libros y no entran en una biblioteca? Podemos tener un lugar donde depositamos los libros que menos usamos, y mantenemos una libretita donde especificamos qué libros dejamos ahí y en que depósito están.
En fin, podemos organizarlos de mil maneras, pero se entiende la idea que organizando los datos vamos a ser más eficientes, no?

## Pilas

Las pilas, como sugiere el nombre, siguen el principio "Último en entrar, primero en salir"  (LIFO). Como si apilamos monedas una encima de la otra, la última moneda que ponemos en la parte superior es la que es la primera que se saca de la pila más tarde.
Para implementar una pila, por lo tanto, necesitamos dos operaciones simples:

* push – agrega un elemento a la parte superior de la pila
* pop – elimina el elemento en la parte superior de la pila

![](../_src/assets/05-Estructuras_Datos_1/ejemplo_pila.jpg)


## Colas

Las colas, como sugiere el nombre, siguen las Primero en entrar primero en salir (FIFO) principio. Como si esperara en una cola las entradas del cine, el primero en hacer fila es el primero en comprar una entrada y disfrutar de la película.

Para implementar una cola, por lo tanto, necesitamos dos operaciones simples:

enqueue – agrega un elemento al final de la cola:
dequeue – elimina el elemento al principio de la cola:

