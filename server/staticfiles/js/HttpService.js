const urlRequest = 'http://127.0.0.1:8000/api';

class HttpService {
    static async DeleteEmployee(id) {
    try{
        let response = await fetch(`${urlRequest}/deleteEmployee/${id}`, {
            method: 'DELETE'
        });
        if (response.ok){
          alert('Сотрудник успешно удалён');
          document.getElementById(`row-${id}`).remove();
        }
        else{
          let msg = `Ошибка удаления (код ${response.status})`
          console.log(msg)
          alert(msg)
        }
        console.log(response.ok)
    }
    catch (error){
        console.error('Ошибка:', error);
    }
  }

  
  static async DeletePosition(id) {
    try{
        let response = await fetch(`${urlRequest}/deletePosition/${id}`, {
            method: 'DELETE'
        });
        if (response.ok){
          alert('Должность успешно удалёна');
        }
        else{
          let msg = `Ошибка удаления, возможно объект уже не существует (код ${response.status})`
          console.log(msg)
          alert(msg)
        }
        document.getElementById(`row-${id}`).remove();
        console.log(response.ok)
    }
    catch (error){
        console.error('Ошибка:', error);
    }
  }
}