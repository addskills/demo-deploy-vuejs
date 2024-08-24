<template>
  <div id="app" class="max-w-md mx-auto p-6 bg-gray-100 min-h-screen">
    <h1 class="text-3xl font-bold mb-4 text-center text-blue-600">Todo App</h1>
    <input 
      v-model="newTodo" 
      @keyup.enter="addTodo" 
      placeholder="Add a new todo"
      class="w-full p-2 mb-4 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
    >
    <ul class="space-y-2">
      <li v-for="(todo, index) in todos" :key="index" class="flex items-center bg-white p-3 rounded shadow">
        <input 
          type="checkbox" 
          v-model="todo.completed"
          class="mr-2 form-checkbox h-5 w-5 text-blue-600"
        >
        <span :class="{ 'line-through text-gray-500': todo.completed }" class="flex-grow">
          {{ todo.text }}
        </span>
        <button @click="removeTodo(index)" class="ml-2 px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500">
          Delete
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTodo: '',
      todos: [
        { text: 'Learn Vue', completed: false },
        { text: 'Build a todo app', completed: false },
        { text: 'Master Vue', completed: false }
      ]
    }
  },
  methods: {
    addTodo() {
      if (this.newTodo.trim().length === 0) {
        return
      }
      this.todos.push({ text: this.newTodo, completed: false })
      this.newTodo = ''
    },
    removeTodo(index) {
      this.todos.splice(index, 1)
    }
  }
}
</script>