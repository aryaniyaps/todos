import { FC } from "react";
import { Helmet } from "react-helmet";
import { Link } from "react-router-dom";
import { Button } from "@nextui-org/react";
import BaseLayout from "../../layouts/BaseLayout";

const LandingPage: FC = () => {
    return (
        <BaseLayout>
            <Helmet>
                <title>Home | Todos</title>
            </Helmet>
            <div
                style={{
                    display: "flex",
                    flexDirection: "column",
                    flexGrow: "grow",
                }}
            >
                {/* hero section */}
                <div className="mx-auto max-w-7xl px-4 sm:my-12 sm:px-6 md:my-16 lg:my-20 lg:px-8 xl:my-28">
                    <div className="mb-4">
                        {/* main title */}
                        <h1 className="text-4xl text-center font-extrabold text-gray-900 sm:text-5xl md:text-6xl leading-none">
                            <span className="block xl:inline">workflow control</span>
                            <span className="block text-accent">made simple</span>
                        </h1>
                        {/* tagline */}
                        <p className="mt-3 text-center text-base sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl">
                            let's plan your workflow, one step at a time!
                        </p>
                    </div>
                    <div className="flex items-center justify-center">
                        <Link to="/dash">
                            <Button>Get started</Button>
                        </Link>
                    </div>
                </div>
                <div className="bg-primary-300 h-full" />
            </div>
        </BaseLayout>
    );
};

LandingPage.displayName = "LandingPage";
export default LandingPage;
