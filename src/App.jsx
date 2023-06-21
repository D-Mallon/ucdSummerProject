import React, { useEffect, useState } from 'react';
import Map from './components/Map';
import './App.css'

const reactLogo = "react.svg"
const viteLogo = "vite.svg"
const appleLogo = "apple.png"
const reactLogoPath = `/static/${reactLogo}`
const viteLogoPath = `/static/${viteLogo}`
const appleLogoPath = `/static/${appleLogo}`

function App() {
  return (
    <div>
      <h1>State of Mind</h1>
      <Map />
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={ viteLogoPath } className="logo" alt="Vite logo" />
        </a>
        <a href="https://reactjs.org" target="_blank">
          <img src={ reactLogoPath } className="logo react" alt="React logo" />
        </a>
      </div>
    </div>
  );
}

export default App;