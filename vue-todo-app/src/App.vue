<template>
  <div id="app" class="max-w-md mx-auto p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Todo App</h1>
    <div class="flex mb-4">
      <input 
        v-model="newTodo" 
        @keyup.enter="addTodo"
        placeholder="Add a new todo" 
        class="flex-grow p-2 border rounded-l focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
      <button 
        @click="addTodo" 
        class="px-4 py-2 bg-blue-500 text-white rounded-r hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        Add
      </button>
    </div>
    <ul class="space-y-2">
      <li v-for="todo in todoStore.todos" :key="todo.id" class="flex items-center bg-white p-3 rounded shadow">
        <input 
          type="checkbox" 
          :checked="todo.completed"
          @change="toggleTodo(todo.id)"
          class="mr-2 form-checkbox h-5 w-5 text-blue-600"
        >
        <span :class="{ 'line-through text-gray-500': todo.completed }" class="flex-grow">
          {{ todo.text }}
        </span>
        <button @click="removeTodo(todo.id)" class="ml-2 px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500">
          Delete
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
import { todoStore } from './todoStore.js'

export default {
  data() {
    return {
      newTodo: '',
      todoStore
    }
  },
  created() {
    this.todoStore.fetchTodos()
  },
  methods: {
    addTodo() {
      this.todoStore.addTodo(this.newTodo)
      this.newTodo = ''
    },
    removeTodo(id) {
      this.todoStore.removeTodo(id)
    },
    toggleTodo(id) {
      this.todoStore.toggleTodo(id)
    }
  }
}
</script>