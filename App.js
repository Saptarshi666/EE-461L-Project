import { Routes,
  Route,
  useNavigate,
  useLocation,
  Navigate,Outlet, Link } from "react-router-dom";

export default function App() {
  const navigate = useNavigate();
  return (
    <div className = 'app'>
      <div className="button-container">
          <span onClick={() => navigate("/login")} className="btn">
              Login
          </span>
          <span onClick={() => navigate("/newuser")} className="btn">
              New User
          </span>
          </div>


    
     
      
      <Outlet />
    </div>
  );
}

