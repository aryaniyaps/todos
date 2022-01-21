import "./styles/main.css";
import { FC, Suspense, lazy } from "react";
import { QueryClientProvider } from "react-query";
import { ThemeProvider } from "@mui/material";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import queryClient from "./lib/queryClient";
import Fallback from "./components/Fallback";

const LandingPage = lazy(() => import("./modules/landing/LandingPage"));
const DashboardPage = lazy(() => import("./modules/dashboard/DashboardPage"));
const RegisterPage = lazy(() => import("./modules/register/RegisterPage"));
const LoginPage = lazy(() => import("./modules/login/LoginPage"));
const NotFoundPage = lazy(() => import("./pages/NotFoundPage"));

const App: FC = () => {
    return (
        <ThemeProvider theme={{}}>
            <QueryClientProvider client={queryClient}>
                <Suspense fallback={<Fallback />}>
                    <BrowserRouter>
                        <Routes>
                            <Route index element={<LandingPage />} />
                            <Route path="/dash" element={<DashboardPage />} />
                            <Route path="/register" element={<RegisterPage />} />
                            <Route path="/login" element={<LoginPage />} />
                            <Route path="*" element={<NotFoundPage />} />
                        </Routes>
                    </BrowserRouter>
                </Suspense>
            </QueryClientProvider>
        </ThemeProvider>
    );
};

App.displayName = "App";
export default App;
