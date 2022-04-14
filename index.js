import { render } from "react-dom";
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import App from "./App";
import HWManagement from "./Components/HWManagement";
import LoginScreen from "./Components/LoginScreen";
import PopUp from "./Components/PopUp";
import ProjPage from "./Components/ProjPage";
import ProjDetails from "./Components/ProjDetails";

const rootElement = document.getElementById("root");
render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />}>
        <Route path="login" element={<LoginScreen />} />
        <Route path="projectpage" element={<ProjPage />} />
        <Route path="newuser" element={<PopUp />} />
        <Route path="hwManagement" element={<HWManagement />} />
        <Route path="projdetails" element={<ProjDetails/>} />
        <Route path="logoff" element={<App/>} />
      </Route>
    </Routes>
  </BrowserRouter>,
  rootElement
);