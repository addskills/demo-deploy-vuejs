import { reactive } from 'vue'

export const todoStore = reactive({
  todos: [
    { text: 'Learn Vue', completed: false },
    { text: 'Build a todo app', completed: false },
    { text: 'Master Vue', completed: false }
  ],
  addTodo(newTodo) {
    if (newTodo.trim().length === 0) {
      return
    }
    this.todos.push({ text: newTodo, completed: false })
  },
  removeTodo(index) {
    this.todos.splice(index, 1)
  }
})
