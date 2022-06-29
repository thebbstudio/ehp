const urlRequest = 'http://127.0.0.1:8000/api';

class HttpService {
  static delete(id) {
      const response = fetch(`${urlRequest}/deleteEmployee`, {
          method: 'DELETE',
          body: {
              id
          }
      })
      return response;
  }
}