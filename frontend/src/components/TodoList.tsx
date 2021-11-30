import { FC } from "react";
import TodoController from "./TodoController";
import TodoItem from "./TodoItem";

const TodoList: FC = () => {
    return (
        <div className="flex flex-col w-full">
            {/* header section */}
            <div className="flex justify-between mb-4">
                <h2>Your todos (12)</h2>
                <TodoController />
            </div>
            {/* todos list */}
            <div className="flex flex-col gap-4">
                {Array.from(Array(10), (_, i) => {
                    return <TodoItem key={i} />;
                })}
            </div>
        </div>
    );
};

TodoList.displayName = "TodoList";
export default TodoList;
