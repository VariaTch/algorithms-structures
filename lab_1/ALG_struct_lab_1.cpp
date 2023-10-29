// ALG_struct_lab_1.cpp
#include <iostream>
#include<stdlib.h>
#include<string>
#include<conio.h>
#include<cmath>
using namespace std;

// двусвязный список
struct Node
{
	int data;
	Node* prev;
	Node* next;
	Node(int data) {
		this->data = data;
		this->prev = this->next = NULL;
	}
};

struct TipList {
	Node* head, * tail;
	TipList() {
		head = tail = NULL;
	}

	~TipList() {
		while (head != NULL) {
			delete_first_elem();
		}
	}

	Node* add_elem_back(int data) {  // добавление элемента в конец списка
		Node* ptr = new Node(data);
		ptr->prev = tail;
		if (tail != NULL)
			tail->next = ptr;
		if (head == NULL)
			head = ptr;
		tail = ptr;
		return ptr;
	}
	Node* add_elem_front(int data) {   // добавление элемента в начало списка
		Node* ptr = new Node(data);
		ptr->next = head;
		if (head != NULL)
			head->prev = ptr;
		if (tail == NULL)
			tail = ptr;
		head = ptr;
		return ptr;
	}

	void delete_first_elem() //удаление первого элемента
	{
		if (head == NULL) return;
		Node* ptr = head->next;  //создаем временный указатель
		if (ptr != NULL)
			ptr->prev = NULL;
		else                     //если удаляем единственный объект, то и tail и head = 0 
			tail = NULL;

		delete head;
		head = ptr;
	}

	void delete_last_elem() {     //удаление последнего элемента
		if (tail == NULL) return;
		Node* ptr = tail->prev;
		if (ptr != NULL)
			ptr->next = NULL;
		else
			head = NULL;
		delete tail;
		tail = ptr;
	}

	Node* get_elem(int index) {    // получение элемента по индексу
		Node* ptr = head;
		int n = 0;
		while (n != index) {
			if (ptr == NULL)
				return ptr;
			ptr = ptr->next;
			n++;
		}
		return ptr;
	}

	void erase_elem(int index) {   //удаление по индексу
		Node* ptr = get_elem(index);
		if (ptr == NULL) return;

		if (ptr->prev == NULL) {
			delete_first_elem();
			return;
		}

		if (ptr->next == NULL) {
			delete_last_elem();
			return;
		}
		Node* left = ptr->prev;
		Node* right = ptr->next;
		left->next = right;
		right->prev = left;
		delete ptr;
	}

	Node* operator[](int index) {   //оператор, возвращающий элемент по индексу
		return get_elem(index);
	}

	Node* insert_elem(int index, int data) {
		Node* right = get_elem(index);
		if (right == NULL)
			return add_elem_front(data);
		Node* left = right->prev;
		if (left == NULL)
			return add_elem_back(data);
		Node* ptr = new Node(data);

		ptr->prev = left;
		ptr->next = right;
		left->next = ptr;
		right->prev = ptr;

		return ptr;
	}

	void show() {
		Node* temp = head;
		while (temp != NULL)
		{
			cout << temp->data << " ";
			temp = temp->next;
		}
	}

	void swap(int index, int index2) {
		Node* temp = head;
		for (int i = 0; i < index; i++) {
			temp = temp->next;
		}
		Node* temp1 = head;
		for (int i = 0; i < index2; i++) {
			temp1 = temp1->next;
		}
		int k = temp->data;
		temp->data = temp1->data;
		temp1->data = k;
	}
};

// динамический массив

class DynamicArray {
private:

	int* array = NULL;
	int size;
	int capacity;

public:
	DynamicArray()
	{
		capacity = 1;
		size = 0;
		array = new int[capacity];
	}

	DynamicArray(int capacity)
	{
		this->capacity = capacity;
		array = new int[capacity];
		size = 0;
	}

	int getSize() { return size; }

	int getCapacity() { return capacity; }

	void push_back(int value)
	{
		if (size == capacity) {

			growArray();
		}

		array[size] = value;
		size++;
	}

	void pop_back()
	{
		array[size - 1] = 0;

		size--;
		if (size == (capacity / 2)) {
			shrinkArray();
		}
	}

	void growArray()
	{
		int* temp = new int[capacity * 2];

		capacity = capacity * 2;
		for (int i = 0; i < size; i++) {
			temp[i] = array[i];
		}

		delete[] array;
		array = temp;
	}


	void shrinkArray()
	{

		capacity = size;
		int* temp = new int[capacity];

		for (int i = 0; i < size; i++) {
			temp[i] = array[i];
		}

		delete[] array;
		array = temp;
	}

	int search(int key)
	{
		for (int i = 0; i < size; i++) {
			if (array[i] == key) {
				return i;
			}
		}
		return -1;
	}

	void insertAt(int index, int value)
	{
		if (size == capacity) {
			growArray();
		}

		for (int i = size - 1; i >= index; i--) {
			array[i + 1] = array[i];
		}

		array[index] = value;
		size++;
	}

	void deleteAt(int index)
	{
		for (int i = index; i < size; i++) {
			array[i] = array[i + 1];
		}

		array[size - 1] = 0;
		size--;

		if (size == (capacity / 2)) {
			shrinkArray();
		}
	}

	void printArrayDetails()
	{
		cout << " Массив : ";
		for (int i = 0; i < size; i++) {
			cout << array[i] << " ";
		}
		cout << endl;
		cout << " Кол-во элементов : " << size
			<< ", capacity :" << capacity << endl;
	}

	bool isEmpty()
	{
		if (size == 0) {
			return true;
		}
		else {
			return false;
		}
	}
};


// стек
string operations = "+=*/-";

struct Stack_struct {   // узел стека
	string symbol;
	Stack_struct* next;
};

struct Stack {
	Stack_struct* tail;
	Stack(): tail(nullptr){}  //конструктор
	bool isEmpty() {
		if (tail == nullptr)return 1;
		return 0;
	}
	void output() {               // выводит содержимое стека на экран
		Stack_struct* curr = tail;
		while (curr) {
			curr = curr->next;
		}
		cout << "\n";
	}
	string pop(bool print = 1) {                  //удаляет и возвращает символ с вершины стека
		if (tail == nullptr) return "END";
		if (print) cout << tail->symbol << " ";
		string answer = tail->symbol;
		Stack_struct* p = new Stack_struct;
		p = tail;
		tail = tail->next;
		p->next = nullptr;
		delete p;
		return answer;
	} 
	void push(string sym) {                     //добавляет новый символ на вершину стека
		Stack_struct* p = new Stack_struct;
		p->symbol = sym;
		p->next = tail;
		tail = p;
	}
};

//приоритеты операций
int prior(char c) {                
	switch (c) {
	case '(': return 1;
	case '+': case '-': return 2;
	case '*': case '/': return 3;
	default: return 0;
	}
}

int action(int& value1, int& value2, string& oper) {
	switch (oper[0]) {
	case '+':
		return value1 + value2;
		break;
	case '-':
		return value1 - value2;
		break;
	case '*':
		return value1 * value2;
		break;
	case '/':
		return value1 / value2;
		break;
	default:
		break;
	}
}

void calculate(string& data, bool prefix) {
	if (prefix) {
		for (int j = data.length() - 1, i = 0; j >= i; --j, ++i) {
			swap(data[j], data[i]);
		}
	}
	
	Stack numbers;
	string num;
	string  sym;
	int val_1, val_2;
	for (int i = 0; i <= data.length(); i++) {
		sym = data[i];
		if (operations.find(sym) != -1) {
			if (prefix) {
				val_1 = stod(numbers.pop(0));
				val_2 = stod(numbers.pop(0));
			}
			else {
				val_2 = stod(numbers.pop(0));
				val_1 = stod(numbers.pop(0));
			}

			numbers.push(to_string(action(val_1, val_2, sym)));
		}
		if (sym >= "0" && sym <= "9" || sym == ".") {
			num += sym;
		}
		if (sym == " ") {
			if (operations.find(data[i - 1]) != -1) continue;
			if (prefix) {
				for (int j = num.length() - 1, i = 0; j >= i; --j, ++i) {
					swap(num[j], num[i]);
				}
			}
			numbers.push(num);
			num.erase(0, num.length());
		}
	}
	numbers.pop(1);
	cout << "\n";
}

void sort_station(string& data, bool print = 1)
{
	Stack stack;
	string note;
	string sym;
	for (int i = 0; i <= data.length(); ++i) {
		if (data[i] == ' ') data.erase(i, 1);
	}
	for (int i = 0; i < data.length(); i++) {
		sym = data[i];
		if (sym >= "0" && sym <= "9" || sym == ".") {
			note += sym;
			if (sym == "." || data[i + 1] == '.' || data[i + 1] >= '0' && data[i + 1] <= '9') continue;
			note += " ";
			if (print) {
				stack.output();
			}
		}
		if (sym == "(") {
			stack.push(sym);
			if (print) {
				stack.output();
			}
			continue;
		}
		if (sym == ")") {
			while (stack.tail->symbol != "(") {
				note += stack.pop(0);
				note += " ";
			}
			stack.pop(0);
			if (print) {
				stack.output();
			}
			continue;
		}
		if (operations.find(sym) != -1) {

			if (stack.isEmpty() || prior(stack.tail->symbol[0] < prior(sym[0]))) {
				stack.push(sym);
				if (print) {
					stack.output();
				}
			}
			else {
				while (!stack.isEmpty() && prior(stack.tail->symbol[0]) >= prior(sym[0])) {
					note += stack.pop(0);
					note += " ";
				}
				stack.push(sym);
				if (print) {
					stack.output();

				}
			}
		}
	}
	if (print) {
		stack.output();

	}
	while (!stack.isEmpty()) {
		note += stack.pop(0);
		note += " ";
	};
	if (print) {
		cout << "\nСтек: ";
	}
	cout << note << "\n";
	data = note;
}

// Конвертирование тригонометрической функции в обратную польскую запись
void convertToRPN_tr(string& expression) 
{
	string rpn;
	bool print = 1;
	Stack stack;

	string sym;
	for (int i = 0; i < expression.length(); i++) 
	{
		char c = expression[i];
		sym = expression[i];
		if (sym >= "0" && sym <= "9" || sym == ".") {
			rpn += sym;
			if (sym == "." || expression[i + 1] == '.' || expression[i + 1] >= '0' && expression[i + 1] <= '9') continue;
			rpn += " ";
			if (print) {
				stack.output();
			}
		}
		// Если символ - буква, то это тригонометрическая функция
		if (isalpha(c)) 
		{
			rpn += c;
			rpn += " ";
		}
		if (sym == "(") 
		{
			stack.push(sym);
			if (print) {
				stack.output();
			}
			continue;
		}
		if (sym == ")") 
		{
			while (stack.tail->symbol != "(") 
			{
				rpn += stack.pop(0);
				rpn += " ";
			}
			stack.pop(0);
			if (print) 
			{
				stack.output();
			}
			continue;
		}
		if (operations.find(sym) != -1) 
		{

			if (stack.isEmpty() || prior(stack.tail->symbol[0] < prior(sym[0]))) 
			{
				stack.push(sym);
				if (print) 
				{
					stack.output();
				}
			}
			else 
			{
				while (!stack.isEmpty() && prior(stack.tail->symbol[0]) >= prior(sym[0])) 
				{
					rpn += stack.pop(0);
					rpn += " ";
				}
				stack.push(sym);
				if (print) 
				{
					stack.output();
				}
			}
		}
	}
	if (print) {
		stack.output();

	}
	while (!stack.isEmpty()) {
		rpn += stack.pop(0);
		rpn += " ";
	};
	if (print) {
		cout << "\nСтек: ";
	}
	cout << rpn << "\n";
	expression = rpn;
}



int main() {
	setlocale(LC_ALL, "ru");
	TipList list;
	int ch = 0;
	int choice_start_menu = 0;  //для основного меню
	int choice_action_list = 0; //для работы со списком
	int choice_list_menu = 0;   //для ввода, вывода списка
	int switcher = 0;           //для работы с сортировочной станцией
	string data = "";

	do {
		cout << "выберите вариант: " << endl;
		cout << "1 - Работа с двусвязным списком" << endl;
		cout << "2 - Стек" << endl;
		cout << "3 - Динамический массив" << endl;
		cout << "4 - Выход из программы" << endl;
		cin >> choice_start_menu;
		int lenght = 0;
		switch (choice_start_menu)
		{
		case 1:
			do {
				cout << "Выберите вариант: " << endl;
				cout << "1 - Вывод рандомного списка " << endl;
				cout << "2 - Работа со списком" << endl;
				cout << "3 - Выход из программы" << endl;

				cin >> choice_list_menu;
				switch (choice_list_menu) {
				case 1:
					cout << "Введите длину списка: " << endl;
					cin >> lenght;
					cout << "Список: ";
					for (int i = 0; i < lenght; i++) {
						int data = rand() % 100;
						list.add_elem_back(data);
					}
					list.show();
					system("pause");
					break;

				case 2:
					do {
						cout << endl << "Выберите действие со списком: " << endl;
						cout << "1 - Вывести элемент списка " << endl;
						cout << "2 - Вставить элемент в любую позицию списка " << endl;
						cout << "3 - Поменять 2 любых элемента в списке " << endl;
						cout << "4 - Удалить любой элемент в списке " << endl;
						cout << "5 - Выход из операций со списком " << endl;

						cin >> choice_action_list;
						switch (choice_action_list) {
						case 1:
							cout << "Исходный список : " << endl;
							list.show();
							cout << endl;
							cout << "Введите индекс элемента, который хотите вывести: ";
							int index;
							cin >> index;
							cout << list[index]->data << endl;
							system("pause");
							break;
						case 2:
							cout << "Исходный список" << endl;
							list.show();
							cout << endl;
							cout << "Введите индекс, а после саму переменную" << endl;
							int data, head;
							cin >> index;
							cin >> data;
							list.insert_elem(index, data);
							list.show();
							system("pause");
							break;
						case 3:
							cout << "Исходный список" << endl;
							list.show();
							cout << endl;
							int index2;
							cout << "Первый индекс" << endl;
							cin >> index;
							cout << "Второй индекс" << endl;
							cin >> index2;
							list.swap(index, index2);
							cout << "Измененный список" << endl;
							list.show();
							system("pause");
							break;
						case 4:
							cout << "Исходный список" << endl;
							list.show();
							cout << "Введите индекс элемента, который хотите удалить " << endl;
							int del;
							cin >> del;
							list.erase_elem(del);
							list.show();
							system("pause");
							break;
						}
					} while (choice_action_list != 5);
					break;
				}
			} while (choice_list_menu != 3);
			break;

		case 2:
			cout << "Выберите действие\n" \
				"1. Конвертировать выражение \n" \
				"2. Вычислить выражение \n"
				"3. Конвертировать тригонометрическое выражение\n" ;
			do
			{
				cout << "Выполнить пункт: ";
				cin >> switcher;
				switch (switcher)
				{
				case 1:
					data.erase(0, data.length());
					cin.ignore();
					cout << "Введите выражение: ";
					getline(cin, data);
					sort_station(data);
					break;
				case 2:
					cout << "Введите конвертированное выражение: ";
					cin.ignore();
					getline(cin, data);
					data += '\0';
					
					calculate(data, 0);
					break;
				case 3:
					cout << "Введите тригонометрическое выражение: ";
					cin.ignore();
					getline(cin, data);
					data += '\0';

					convertToRPN_tr(data);
					
					break;
				}
			} while (switcher != 3);
			break;
		case 3:
			cout << "Поехали" << endl;
			DynamicArray da;
			int size, i;
			cout << " Введите количество элементов массива: " << endl;
			cin >> size;
			for (i = 0; i < size; i++) {
				da.push_back(rand() % 100);
			}

			da.printArrayDetails();
			int e;
			do {
				cout << " Выберите действие: " << endl;
				cout << "1) Вставка" << endl;
				cout << "2) Получение индекса элемента " << endl;
				cout << "3) Удаление элемента по индексу " << endl;
				cout << "4) Удаление последнего элемента  " << endl;
				cout << "5) Выход " << endl;

				cin >> e;

				switch (e)
				{
				case 1:
				{
					int index, value;
					cout << "Введите индекс , куда необходимо вставить элемент " << endl;
					cin >> index;
					cout << "Введите элемент " << endl;
					cin >> value;
					da.insertAt(index, value);
					da.printArrayDetails();
				}
				break;
				case 2:
				{
					int value;
					cout << "Введите элемент который хотите получить " << endl;
					cin >> value;
					int index = da.search(value);
					if (index != -1) {
						cout << "Element found at index : " << index << endl;
					}
					else {
						cout << "Element not found " << endl;
					}
				}
				break;
				case 3:
				{
					int index;

					cout << "Введите индекс элемента, который хотите удалить " << endl;
					cin >> index;
					da.deleteAt(index);
					da.printArrayDetails();
				}
				break;
				case 4:
				{
					cout << "Удаление последнего элемента  " << endl;
					da.pop_back();
					da.printArrayDetails();
				}
				break;
				case 5:
				{
					break;
				}
				break;

				}
			} while (e != 5);
			break;
		}

	}while (choice_start_menu != 4);
	return 0;
}