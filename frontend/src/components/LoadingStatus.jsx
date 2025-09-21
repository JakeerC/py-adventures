/**
 * LoadingStatus Component
 *
 * Simple loading indicator component that displays a spinner and loading message
 * while story generation or loading operations are in progress.
 *
 * Features:
 * - Displays themed loading message
 * - Animated spinner for visual feedback
 * - Informative text about the loading process
 * - Consistent styling with the application theme
 *
 * @component
 * @param {Object} props - Component props
 * @param {string} props.theme - The theme name to display in the loading message
 * @returns {JSX.Element} The loading status interface with spinner and message
 */
function LoadingStatus({ theme }) {
  return (
    <div className="loading-container">
      <h2>Generating Your {theme} Story</h2>

      <div className="loading-animation">
        <div className="spinner"></div>
      </div>

      <p className="loading-info">
        Please wait while we generate your story...
      </p>
    </div>
  );
}

export default LoadingStatus;
