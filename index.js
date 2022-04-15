import { render } from "react-dom";
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import App from "./App";
import LoginScreen from "./Components/LoginScreen";
import PopUp from "./Components/PopUp";
import ProjPage from "./Components/ProjPage";
import HWManagement from "./Components/HWManagement";
import Datasets from "./Components/Datasets";
import SetsDatas from "./Components/setdata";

const rootElement = document.getElementById("root");
render(
  // <CookiesProvider>
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />}>
        <Route path="login" element={<LoginScreen />} />
        <Route path="projectpage" element={<ProjPage />} />
        <Route path="newuser" element={<PopUp />} />
        <Route path="HWManagement" element={<HWManagement />} />
        <Route path="Datasets" element={<Datasets />} />
        <Route path="SetsDatas" element={<SetsDatas />} />
      </Route>
    </Routes>
  </BrowserRouter>,
  //  </CookiesProvider>, 
  rootElement
);