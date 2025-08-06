import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Fruit1 from './components/Fruit1'
import Fruit2 from './components/Fruit2'
import Fruit3 from './components/fruit3'
import Fruit4 from './components/fruit4'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <Fruit1 />
      <Fruit2 />
      <Fruit3 />
      <Fruit4 />
    </div>
  )
}

export default App
