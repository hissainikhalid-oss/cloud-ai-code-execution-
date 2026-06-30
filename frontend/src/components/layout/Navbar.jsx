import "../../styles/layout/navbar.css";

function Navbar() {
    return (
        <nav className="navbar">
            <div className="logo">
                Cloud AI
            </div>

            <ul className="nav-links">
                <li>Home</li>
                <li>About</li>
                <li>Documentation</li>
            </ul>
        </nav>
    );
}

export default Navbar;