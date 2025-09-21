import { useState } from "react";

/**
 * ThemeInput Component
 *
 * Form component for collecting story themes from users.
 * Provides input validation and submission handling for story generation.
 *
 * Features:
 * - Text input for story theme with placeholder suggestions
 * - Form validation to ensure theme is not empty
 * - Error display for validation failures
 * - Submit handler that calls parent component's onSubmit function
 * - Responsive styling with error states
 *
 * @component
 * @param {Object} props - Component props
 * @param {Function} props.onSubmit - Callback function called when form is submitted with theme
 * @returns {JSX.Element} The theme input form interface
 */
function ThemeInput({ onSubmit }) {
  const [theme, setTheme] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!theme.trim()) {
      setError("Please enter a theme name");
      return;
    }

    onSubmit(theme);
  };

  return (
    <div className="theme-input-container">
      <h2>Generate Your Adventure</h2>
      <p>Enter a theme for your interactive story</p>

      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <input
            type="text"
            value={theme}
            onChange={(e) => setTheme(e.target.value)}
            placeholder="Enter a theme (e.g. prirates, space, medieval...)"
            className={error ? "error" : ""}
          />
          {error && <p className="error-text">{error}</p>}
        </div>
        <button type="submit" className="generate-btn">
          Generate Story
        </button>
      </form>
    </div>
  );
}

export default ThemeInput;
