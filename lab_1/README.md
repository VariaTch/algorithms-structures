# algorithms-structures
Сложность https://github.com/VariaTch/algorithms-structures/blob/main/ALG_struct_lab_1.cpp#L33 в худшем случае O(1), потому что независимо от количества элементов в списке, функция выполняет фиксированное количество операций для добавления нового узла в конец.

Сложность https://github.com/VariaTch/algorithms-structures/blob/main/ALG_struct_lab_1.cpp#L188 в худшем случае O(n), потому что тогда вставляемый индекс равен индексу последнего элемента, все N элементов массива должны быть сдвинуты, что занимает O(N) времени. 

Сложность  https://github.com/VariaTch/algorithms-structures/blob/main/ALG_struct_lab_1.cpp#L467 в худшем случае O(n), потому что каждый элемент введенной строки обрабатывается один раз, а операции внутри цикла выполняются за константное время (например все операции с стеком push, pop и тд).
