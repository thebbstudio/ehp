const urlRequest = 'http://127.0.0.1:8000/api';

class HttpService {
    static async DeleteEmployee(id) {
    try{
      // Создание запроса на удаление сотрудника по id с методом delete
      let response = await fetch(`${urlRequest}/deleteEmployee/${id}`, {
          method: 'DELETE'
      });

      // Если ответ 2**, то всё прошло успешно 
      if (response.ok){
        // Сообщаем пользователю и удаляем строку по ID
        alert('Сотрудник успешно удалён');
        document.getElementById(`row-${id}`).remove();
      }
      else{
        // Что-то пошло не так, сообщаем о проблеме и живём дальше
        alert(`Ошибка удаления (код ${response.status})`)
      }
    }
    catch (error){
      console.error('Ошибка:', error);
    }
  }

  
  static async DeletePosition(id) {
    try{
      // Создание запроса на удаление сотрудника по id с методом delete
      let response = await fetch(`${urlRequest}/deletePosition/${id}`, {
          method: 'DELETE'
      });

      // Если ответ 2**, то всё прошло успешно 
      if (response.ok){
        // Сообщаем пользователю и удаляем строку по ID
        alert('Должность успешно удалёна');
        document.getElementById(`row-${id}`).remove();
      }
      else{
        // Что-то пошло не так, сообщаем о проблеме и живём дальше
        alert(`Ошибка удаления (код ${response.status})`)
      }
    }
    catch (error){
      console.error('Ошибка:', error);
    }
  }
}