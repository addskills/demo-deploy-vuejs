import { reactive } from 'vue'

const API_URL = import.meta.env.VITE_API_URL

export const todoStore = reactive({
  todos: [],
  
  async fetchTodos() {
    try {
      const response = await fetch(`${API_URL}/todos`)
      this.todos = await response.json()
    } catch (error) {
      console.error('Error fetching todos:', error)
    }
  },

  async addTodo(newTodo) {
    if (newTodo.trim().length === 0) return

    try {
      const response = await fetch(`${API_URL}/todos`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: newTodo, completed: false })
      })
      const addedTodo = await response.json()
      this.todos.push(addedTodo)
    } catch (error) {
      console.error('Error adding todo:', error)
    }
  },

  async removeTodo(id) {
    try {
      await fetch(`${API_URL}/todos/${id}`, { method: 'DELETE' })
      this.todos = this.todos.filter(todo => todo.id !== id)
    } catch (error) {
      console.error('Error removing todo:', error)
    }
  },

  async toggleTodo(id) {
    try {
      const todo = this.todos.find(t => t.id === id)
      const response = await fetch(`${API_URL}/todos/${id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: todo.text, completed: !todo.completed })
      })
      const updatedTodo = await response.json()
      Object.assign(todo, updatedTodo)
    } catch (error) {
      console.error('Error toggling todo:', error)
    }
  }
})