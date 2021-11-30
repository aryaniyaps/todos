import { FC } from "react";
import Button from "./Button";

const TodoController: FC = () => {
    return (
        <div className="flex">
            <Button>add todo</Button>
        </div>
    );
};

TodoController.displayName = "TodoController";
export default TodoController;
