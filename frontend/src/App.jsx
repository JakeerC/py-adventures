import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import StoryLoader from "./components/StoryLoader";
import StoryGenerator from "./components/StoryGenerator";

function App() {
  return (
    <Router>
      <div className="app-container">
        <header>
          <h1>Interactive Story Generator</h1>
          <main>
            <Routes>
              <Route path={"/story/:id"} element={<StoryLoader />} />
              <Route path={"/"} element={<StoryGenerator />} />
            </Routes>
          </main>
        </header>
      </div>
    </Router>
  );
}

export default App;
